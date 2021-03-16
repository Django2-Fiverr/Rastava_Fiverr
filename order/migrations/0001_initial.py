# Generated by Django 2.2.19 on 2021-03-14 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gig', '0003_auto_20210312_1258'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False, verbose_name='پرداخت شده / نشده')),
                ('date_of_payment', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='خریدار')),
            ],
            options={
                'verbose_name': 'سبد خرید کاربر',
                'verbose_name_plural': 'سبد های خرید کاربران',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.BooleanField(default=False, verbose_name='منقضی شده / نشده')),
                ('delivery_status', models.BooleanField(default=False, verbose_name='وضعیت/ تحویل')),
                ('date_of_transaction', models.DateTimeField(verbose_name='زمان انجام معامله')),
                ('deadline', models.DateTimeField(verbose_name='مهلت تحویل')),
                ('file', models.FileField(blank=True, null=True, upload_to=order.models.get_name, verbose_name='فایل ارسالی')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='خریدار')),
                ('gig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gig.Gig', verbose_name='گیگ مورد معامله')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_transaction', to=settings.AUTH_USER_MODEL, verbose_name='فروشنده')),
            ],
            options={
                'verbose_name': 'معامله',
                'verbose_name_plural': 'معاملات',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.IntegerField(verbose_name='مهلت تحویل سفارش')),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gig.Gig', verbose_name='گیگ مرد نظر')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='سبد خرید')),
            ],
            options={
                'verbose_name': 'جزپیات محصول',
                'verbose_name_plural': 'جزپیات محصولات',
            },
        ),
    ]