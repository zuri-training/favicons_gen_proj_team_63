from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

User = settings.AUTH_USER_MODEL


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    # full_name = models.CharField(max_length=255, blank=True, null=True)
    # slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    def __str__(self):
        return self.email
    
    def get_full_name(self) -> str:
        return super().get_full_name()

    def get_short_name(self) -> str:
        return super().get_short_name()



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return f"user_{instance.uploaded_by.id}/{filename}"


class Image(models.Model):
    # url = models.URLField()
    uploaded_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    favourite = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='image_info')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Favicon(models.Model):
    image = models.OneToOneField(to=Image, null=True, on_delete=models.CASCADE)
    original_filename = models.CharField(max_length=256, null=True)
    new_filename = models.CharField(max_length=256, null=True)
    file_type = models.CharField(max_length=10, null=True)
    file_byte_size = models.IntegerField(default=0)
    embed_link = models.TextField(null=True)