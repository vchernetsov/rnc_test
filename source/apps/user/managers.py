from django.contrib.auth.models import UserManager as _UserManager


class UserManager(_UserManager):

    @property
    def available(self):
        queryset = self.filter(is_active=True)
        return queryset
