from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    # native_name = models.CharField(max_length=5)

    USERNAME_FIELD = "email" # Making this the primary identifier
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    class Meta:
        ordering =  ["email"] # The default ordering for the object, for use when obtaining lists of objects
        # verbose_name = "User" # The name that shows up in the admin panel

    def __str__(self):
        return f"{self.email}"
