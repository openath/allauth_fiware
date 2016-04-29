# allauth_fiware
Django-allauth app to provide "login with FIWARE"

Django-allauth is a popular package providing easy logins to many social networks.    FIWARE's Keyrock component is an OAuth provider.   When
we wanted to create a Django app which could login with FIWARE, we found allauth was the easiest and most powerful to work with.

This app can be included in a project and listed in INSTALLED_APPS.
We recommend first getting things 100% working with a couple of major
social logins (we used Facebook and Google), then adding this app.

A SocialAccount record must be created in the admin, and the keys copied
from the Keyrock user interface.

    INSTALLED_APPS = (
        ...
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',
        'allauth.socialaccount.providers.google',
        'project.oauth_fiware',  #must be after socialaccount
        ...
    )


As a demonstration, if you have a FIWARE lab account, you can log in at
    https://opentrack.info/accounts/login/

    