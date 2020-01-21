from django.contrib import admin as default_admin
from django.utils.translation import gettext as _


class AdminSite(default_admin.AdminSite):
    site_header = _('ToS service administration')
    index_title = _('ToS service admin')


admin = AdminSite(name='site')
