from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from apps.user import managers


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )

    street = models.CharField(_('street'), max_length=1024, blank=True, null=True)
    post_code = models.CharField(_('post code'), max_length=1024, blank=True, null=True)

    class Meta:
        ordering = ['date_joined', ]

    def __str__(self):
        return self.username

    objects = managers.UserManager()

