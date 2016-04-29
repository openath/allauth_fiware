from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import FiwareProvider

urlpatterns = default_urlpatterns(FiwareProvider)
