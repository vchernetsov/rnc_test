from rest_framework import viewsets
from apps.tos import models
from apps.tos import serializers


class TOSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.SignedTOS.objects.all()
    serializer_class = serializers.TOSSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
