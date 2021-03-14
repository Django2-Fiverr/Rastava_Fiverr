from azbankgateways import bankfactories, models as bank_models, default_settings as settings

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import datetime_safe

from order.models import Order
from order.views import create_transaction
from extensions.constants import CATEGORY


@login_required
def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    order:Order = Order.objects.filter(owner_id=request.user.id , paid=False).first()
    if order:
        amount = order.get_total_payment_price()*10
    else:
        raise Http404
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    bank = factory.create()  # or factory.create(bank_models.BankType.BMI) or set identifier
    bank.set_request(request)
    bank.set_amount(amount)
    # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
    bank.set_client_callback_url('/payment/callback-gateway/')
    bank.set_mobile_number(user_mobile_number)  # اختیاری

    # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
    # پرداخت برقرار کنید. 
    bank_record = bank.ready()

    # هدایت کاربر به درگاه بانک
    return bank.redirect_gateway()


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        # return HttpResponse("پرداخت با موفقیت انجام شد.")
        return render(request, 'success.html')
    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.
    # return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت ۴۸ ساعت پول به حساب شما بازخواهد گشت.")
    order = Order.objects.filter(owner_id=request.user.id,paid=False).first()
    if order:
        order.paid = True
        order.date_of_payment = datetime_safe.datetime.now()
        order.save()
        create_transaction(request,order)

    return render(request, 'cancle.html',{'categories':CATEGORY})
