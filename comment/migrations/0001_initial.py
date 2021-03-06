from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=400, verbose_name='متن پیام')),
                ('publish', models.DateTimeField(auto_now_add=True, null=True, verbose_name='متن پیام')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
