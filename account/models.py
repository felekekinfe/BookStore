from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100,unique=True)

    registered_on = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #registration_ip = models.CharField(max_length=100,blank=False)
    #last_login_ip = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','last_name','username','phone']