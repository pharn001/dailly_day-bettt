from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager
# Create your models here.
class BlogPost(AbstractBaseUser, PermissionsMixin):
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    # published_date = models.DateTimeField(auto_now_add=True)
    email=models.EmailField(max_length=255, unique=True, verbose_name=_("Email Address"))
    first_name=models.EmailField(max_length=255, verbose_name=_("Email Address"))
    Last_name=models.EmailField(max_length=255, verbose_name=_("Email Address"))

    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined =models.DateTimeField(auto_now_add=True)
    last_login =models.DateTimeField(auto_now=True)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name"]
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.Last_name}"
    def tokens(self):
        pass