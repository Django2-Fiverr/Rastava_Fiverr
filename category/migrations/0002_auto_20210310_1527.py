# Generated by Django 2.2.19 on 2021-03-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Write a topic ex:photo edit, programming,...', max_length=50),
        ),
    ]
