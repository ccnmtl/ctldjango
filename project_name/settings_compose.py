# flake8: noqa
from {{project_name}}.settings_shared import *
from ctlsettings.compose import common

locals().update(
    common(
        project=project,
        base=base,
        STATIC_ROOT=STATIC_ROOT,
        INSTALLED_APPS=INSTALLED_APPS,
    ))

try:
    from {{project_name}}.local_settings import *
except ImportError:
    pass
