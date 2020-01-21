"""Serializers collection for TOS application"""
from rest_framework import serializers
from apps.tos.models import SignedTOS

class TOSSerializer(serializers.ModelSerializer):
    """
    Serializer for TOS model.
    """
    text = serializers.SerializerMethodField()

    class Meta:
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "street",
            "post_code",
            "text",
            "created_at",
        ]
        model = SignedTOS

    def text(self, obj):
        return obj.text
