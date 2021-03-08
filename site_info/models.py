from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=80, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=50, verbose_name='موضوع')
    message = models.CharField(max_length=1000, verbose_name='متن پیام')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    class Meta:
        ordering = ("-date",)
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.full_name


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'درباره ی ما'
        verbose_name_plural = 'درباره ی ما'

    def __str__(self):
        return self.title
