from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from filepreviews import FilePreviews
from jsonfield import JSONField
from model_utils import FieldTracker
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.wagtailcore.models import Site
from wagtail.wagtaildocs.models import AbstractDocument

from .settings import previews_options_callback


@register_setting
class FilePreviewsSettings(BaseSetting):
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'FilePreviews'

    @property
    def is_enabled(self):
        return self.api_key and self.api_secret


class AbstractPreviewableDocument(AbstractDocument):
    preview_data = JSONField(blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _('document')


class PreviewableDocument(AbstractPreviewableDocument):
    admin_form_fields = [
        'title',
        'file',
        'collection',
        'tags',
        'preview_data'
    ]

    tracker = FieldTracker(fields=['file'])


@receiver(post_save, sender=PreviewableDocument)
def document_save(sender, instance, created, **kwargs):
    previous_file = instance.tracker.previous('file')
    file_changed = previous_file != instance.file
    should_generate_preview = False

    if created and file_changed:
        should_generate_preview = True

    if not created and file_changed:
        should_generate_preview = True

    if not should_generate_preview:
        return

    site = Site.objects.get(is_default_site=True)
    settings = FilePreviewsSettings.for_site(site)

    if settings.is_enabled:
        fp = FilePreviews(
            api_key=settings.api_key,
            api_secret=settings.api_secret
        )

        host_url = site.root_url
        document_url = '{}{}'.format(host_url, instance.url)
        callback_url = '{}{}'.format(host_url, reverse('filepreviews_webhook'))

        options = {
            'callback_url': callback_url,
            'data': {
                'document_id': instance.pk
            }
        }

        options.update(previews_options_callback(instance))
        fp.generate(document_url, **options)
