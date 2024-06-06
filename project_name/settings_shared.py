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
    'markdownify.apps.MarkdownifyConfig',

    '{{project_name}}.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7
