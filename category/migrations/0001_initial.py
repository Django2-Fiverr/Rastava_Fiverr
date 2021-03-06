# Generated by Django 2.2.19 on 2021-03-10 11:02

import category.models
from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='عنوان')),
                ('image', models.ImageField(blank=True, null=True, upload_to=category.models.get_name, verbose_name='تصویر')),
                ('content', models.TextField(blank=True, max_length=300, null=True, verbose_name='توضیحات')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Category', verbose_name='موضوع')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ('title',),
            },
        ),
    ]
