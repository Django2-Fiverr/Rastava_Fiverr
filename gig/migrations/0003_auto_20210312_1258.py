# Generated by Django 2.2.19 on 2021-03-12 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0002_gig_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='cost',
            field=models.PositiveIntegerField(verbose_name='قیمت'),
        ),
    ]
