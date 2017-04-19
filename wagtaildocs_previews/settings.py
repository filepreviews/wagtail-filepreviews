from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import six
from django.utils.module_loading import import_string


def get_callback_function(setting_name, default=None):
    func = getattr(settings, setting_name, None)

    if not func:
        return default

    if callable(func):
        return func

    if isinstance(func, six.string_types):
        func = import_string(func)

    if not callable(func):
        raise ImproperlyConfigured(
            '{name} must be callable.'.format(name=setting_name)
        )

    return func


def _get_previews_options(instance):
    return {}


previews_options_callback = get_callback_function(
    'WAGTAILDOCS_PREVIEWS_OPTIONS_CALLBACK',
    default=_get_previews_options
)
