from django.urls import include, path
from rest_framework import routers
from apps.tos.views import sign_view, sign_view_action
from apps.tos.api import TOSViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('tos', TOSViewSet)

urlpatterns = [
    path('admin/sign-agreement', sign_view, name='sign-agreement'),
    path('admin/sign-agreement-action', sign_view_action, name='sign-agreement-action'),
    path(r'', include(router.urls)),
]

