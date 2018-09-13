# flake8: noqa
from {{project_name}}.settings_shared import *

try:
    from {{project_name}}.local_settings import *
except ImportError:
    pass
