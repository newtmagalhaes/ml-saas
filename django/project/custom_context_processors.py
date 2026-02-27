from django.conf import settings


def project_title(request):
    return {
        # TODO: gerar título dinamicamente pela view
        'PROJECT_TITLE': 'MedHealth',
        'PROJECT_NAME': 'MedHealth',
        'DEFAULT_PROJECT_TITLE': 'MedHealth'
    }


def auth_urls(request):
    return {
        'LOGIN_URL': settings.LOGIN_URL,
        'LOGOUT_URL': settings.LOGOUT_URL,
    }
