from django.db import models
from django.contrib.auth.models import AbstractUser
from reviews.models import Reviews
# from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    username = models.CharField(verbose_name='Ник', unique=True)  # Убираем стандартное поле username
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    # phone_number = models.CharField(max_length=20, blank=True, null=True, unique=False)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12, unique=True,error_messages={'unique': "Пользователь с таким именем уже существует!!!",},)

    first_name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(blank=True, null=True)  # разрешаем пустое значение
    count_comments = models.PositiveSmallIntegerField(verbose_name='Колличество комментариев может оставить', default=1, blank=True, null=True)

    USERNAME_FIELD = 'phone_number'  # Указываем, что phone_number теперь используется как идентификатор
    REQUIRED_FIELDS = ['first_name', 'username']  # Поля, запрашиваемые при создании суперпользователя

    def __str__(self):
        return self.phone_number


    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    # def __str__(self):
    #     return self.username

