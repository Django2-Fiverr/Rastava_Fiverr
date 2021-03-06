from django.db import models

from category.models import Skills
from extensions.mainObjects import User
from extensions.functions import split_name


# This function changes default file name and uses the same format ( one.jpg -> two.jpg )
# it returns an address to save the uploaded image file
def get_name(instance, file_name):
    name, ext = split_name(file_name)
    rep = (num for num in range(1000))
    new_name = '{}/{}-{}{}'.format(instance.user.username, instance.user.username, rep.__next__(), ext)
    return 'users/{}'.format(new_name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')
    bio = models.TextField(max_length=3000, blank=True, null=True, help_text='User bio', verbose_name='بیوگرافی')
    birth = models.DateField('Birth', null=True, blank=True)
    skills = models.ManyToManyField(Skills, default='نامشخص', help_text='Choose Your Skills', blank=True,
                                    verbose_name='مهارت ها')
    image = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='تصویر')
    last_update = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل کاربران'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f'/profile/{self.user.id}'

    def show_skills(self):
        skills = self.skills.all()
        if skills:
            skills = list(map(str, skills))
            return ' , '.join(skills)
        return 'وارد نشده'

    show_skills.short_description = 'مهارت های کاربر'
