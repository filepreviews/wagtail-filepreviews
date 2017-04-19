from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls

from wagtaildocs_previews import urls as wagtaildocs_urls

urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'', include(wagtail_urls)),
]
