from django.conf import settings


def project_title(request):
    return {
        # TODO: gerar título dinamicamente pela view
        'PROJECT_TITLE': 'ML SaaS',
        'PROJECT_NAME': 'SaaS',
        'DEFAULT_PROJECT_TITLE': 'ML SaaS'
    }


def auth_urls(request):
    return {
        'LOGIN_URL': settings.LOGIN_URL,
        'LOGOUT_URL': settings.LOGOUT_URL,
    }
