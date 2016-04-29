import requests

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
                                                          OAuth2LoginView,
                                                          OAuth2CallbackView)
from .provider import FiwareProvider


class FiwareOAuth2Adapter(OAuth2Adapter):
    provider_id = FiwareProvider.id
    access_token_url = 'https://account.lab.fiware.org/oauth2/token'
    authorize_url = 'https://account.lab.fiware.org/oauth2/authorize'
    profile_url = 'https://account.lab.fiware.org/user'
    basic_auth = True

    def complete_login(self, request, app, token, **kwargs):
        """
        According to FIWARE docs...
          GET /user?access_token=2YotnFZFEjr1zCsicMWpAA

        gives you this kind of stuff:

          {
            id: 1,
            displayName: "Demo user",
            email: "demo@fiware.org",
            roles: [
              {
                id: 15,
                name: "Manager"
              },
              {
                id: 7
                name: "Ticket manager"
              }
            ],
            organizations: [
              {
                 id: 12,
                 name: "Universidad Politecnica de Madrid",
                 roles: [
                   {
                     id: 14,
                     name: "Admin"
                   }
                ]
              }
            ]
          }


        We need to customize what we pull out
        """



        resp = requests.get(self.profile_url, params={'access_token': token})
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth2_login = OAuth2LoginView.adapter_view(FiwareOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(FiwareOAuth2Adapter)
