# Generated by Django 2.2.17 on 2021-02-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proFile', '0002_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]