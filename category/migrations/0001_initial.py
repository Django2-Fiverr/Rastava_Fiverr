# Generated by Django 2.2.19 on 2021-03-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Write a topic ex:photo edit, programming,...', max_length=20)),
            ],
            options={
                'verbose_name': 'موضوع',
                'verbose_name_plural': 'موضوع ها',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='مهارت')),
            ],
            options={
                'verbose_name': 'مهارت',
                'verbose_name_plural': 'مهارت ها',
            },
        ),
    ]
