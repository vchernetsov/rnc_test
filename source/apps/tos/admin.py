from settings.admin import admin
from apps.tos import models
from django.contrib.admin import ModelAdmin


class TOSAdmin(ModelAdmin):
    list_display = ["first_name", "last_name", "created_at", ]
    search_fields = ["first_name", "last_name", ]
    readonly_fields = [
        "created_at",
        "user",
        "first_name",
        "last_name",
        "street",
        "post_code",
        "signed_file",
    ]

admin.register(models.SignedTOS, TOSAdmin)
