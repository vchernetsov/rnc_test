import os
import uuid
import zlib
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

def signed_file_path(instance, filename):
    user_uuid = instance.user.pk
    signed_at_date = instance.created_at.strftime("%Y-%m-%d")
    signed_at_time = instance.created_at.strftime("%H-%M-%S")
    output = f'tos/{user_uuid}/{signed_at_date}/{signed_at_time}/{filename}'
    return output


class SignedTOS(models.Model):
    HELP_TEXT_UUID = _("Entry id")
    HELP_TEXT_CREATED_AT = _("Date and time when entry was created")
    HELP_TEXT_UPDATED_AT = _("Date and time when entry was updated")

    uuid = models.UUIDField(
        _('UUID'),
        primary_key=True,
        default=uuid.uuid4,
        db_index=True,
        editable=False,
        help_text=HELP_TEXT_UUID
    )

    created_at = models.DateTimeField(
        _('Created at'),
        help_text=HELP_TEXT_CREATED_AT
    )

    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    street = models.CharField(_('street'), max_length=1024, blank=True, null=True)
    post_code = models.CharField(_('post code'), max_length=1024, blank=True, null=True)
    signed_file = models.FileField(upload_to=signed_file_path)

    def text(self):
        absname = os.path.join(settings.MEDIA_ROOT, self.signed_file.path)
        with open(absname, "rb") as fh:
            text = fh.read()
            decompressed = zlib.decompress(text)
        return decompressed

    class Meta:
        ordering = ["created_at", ]
        verbose_name = _('Signed TOS entry')
        verbose_name_plural = _('Signed TOS entries')
