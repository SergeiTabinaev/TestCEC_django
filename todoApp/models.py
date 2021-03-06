from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.urls import reverse


class UserApp(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)


class Category(models.Model):
    """ модель категорий тасок """
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Task(models.Model):
    """модель таски"""
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

