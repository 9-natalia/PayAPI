from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_stuff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_stuff") is not True:
            raise ValueError("El superusuario necesita que is_stuff sea True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario necesita que is_superuser sea True")

        return self.create_superuser(email = email, password = password, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80, unique=True, default="no@gmail.com")
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.email