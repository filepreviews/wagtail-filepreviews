from django.conf.urls import url
from wagtail.wagtailcore import hooks

from .views import filepreviews_webhook


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^documents/webhooks/filepreviews$',
            filepreviews_webhook, name='filepreviews_webhook'),
    ]
