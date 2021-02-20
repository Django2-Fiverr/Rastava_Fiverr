# Generated by Django 2.2.17 on 2021-02-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(help_text='User bio', max_length=1000)),
                ('birth', models.DateField(blank=True, null=True, verbose_name='Birth')),
                ('image', models.ImageField(upload_to='')),
                ('skills', models.ManyToManyField(blank=True, help_text='Choose Your Skills', to='category.Category')),
            ],
        ),
    ]
