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

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

MIDDLEWARE += [
    'django.middleware.csrf.CsrfViewMiddleware',
]

INSTALLED_APPS += [  # noqa
    'django_bootstrap5',
    'django_extensions',
    'markdownify.apps.MarkdownifyConfig',

    '{{project_name}}.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7
