import random
import os
import datetime


def re_format_price(price):
    counter = 1
    temp_var = list()
    for num in reversed(str(price)):
        if counter % 3 == 0:
            temp_var.append(num)
            temp_var.append('/')
        else:
            temp_var.append(num)
        counter += 1
    result = ''.join(reversed(temp_var))
    return result.strip('/')


def get_random_items(obj_class, count):
    obj = obj_class.objects.all()
    result = random.sample(list(obj), count)
    return result


def split_name(file_name):
    base_name = os.path.basename(file_name)
    name, ext = os.path.splitext(base_name)
    return name, ext


def remaining_time(obj):
    date = obj.deadline.date()
    time = obj.deadline.time()
    result = datetime.datetime.combine(date, time) - datetime.datetime.now()
    if result.days < 0:
        obj.expiration = True
        obj.save()
    return result.days


def get_total_price(obj):
    summation = 0
    for item in obj.orderdetail_set.all():
        summation += item.price
    return summation


def create_time_object(time, deadline):
    delta = datetime.timedelta(days=deadline)
    return time + delta
