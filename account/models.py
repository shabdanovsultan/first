from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Поле email не может быть пустым')
        email = self.normalize_email(email)
        user = models(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_active', True)
        return self._create(email, password, **extra_fields)
    
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'name', 'email']

    def get_full_name(self):
        return f'{self.name} {self.last_name}'


    def __str__(self):
        return self.email