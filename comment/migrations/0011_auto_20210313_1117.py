# Generated by Django 2.2.19 on 2021-03-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_auto_20210312_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='تاریخ انتشار'),
        ),
    ]
