# Django settings for {{project_name}} project.
import os.path
from ctlsettings.shared import common

project = '{{project_name}}'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    '{{project_name}}.main',
]

USE_TZ = True

INSTALLED_APPS += [  # noqa
    'django_cas_ng',
    'bootstrap4',
    'infranil',
    'django_extensions',

    '{{project_name}}.main',
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend'
]

CAS_SERVER_URL = 'https://cas.columbia.edu/cas/'
CAS_VERSION = '3'
CAS_ADMIN_REDIRECT = False

# Translate CUIT's CAS user attributes to the Django user model.
# https://cuit.columbia.edu/content/cas-3-ticket-validation-response
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_RENAME_ATTRIBUTES = {
    'givenName': 'first_name',
    'lastName': 'last_name',
    'mail': 'email',
}


THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7
