# Generated by Django 2.2.19 on 2021-02-26 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        ('proFile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentProfile', to='proFile.Profile'),
        ),
    ]
