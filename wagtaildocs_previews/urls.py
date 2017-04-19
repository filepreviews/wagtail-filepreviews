from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from wagtail.wagtaildocs import urls as wagtaildocs_urls

from .views import filepreviews_webhook

urlpatterns = [
    url(r'', include(wagtaildocs_urls)),
    url(r'webhooks/filepreviews$',
        filepreviews_webhook, name='filepreviews_webhook'),
]
