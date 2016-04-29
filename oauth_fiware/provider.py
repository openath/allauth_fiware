from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class FiwareAccount(ProviderAccount):

    def get_avatar_url(self):
        return None

    def to_str(self):
        dflt = super(FiwareAccount, self).to_str()
        return self.account.extra_data.get('name', dflt)


class FiwareProvider(OAuth2Provider):
    id = 'fiware'
    name = 'Fiware'
    account_class = FiwareAccount

    def get_auth_params(self, request, action):
        data = super(FiwareProvider, self).get_auth_params(request, action)
        data['type'] = 'web_server'
        return data

    def extract_uid(self, data):
        # data = data['identity']
        return str(data['id'])

    def extract_common_fields(self, data):
        # data = data['identity']
        return dict(
            email=data.get('email'),
            username=data.get('email'),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            name= data.get('displayName', ''),
        )


providers.registry.register(FiwareProvider)
