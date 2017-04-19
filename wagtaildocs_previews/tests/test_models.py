import json

from django.core.files.base import ContentFile
from django.test import TestCase
from django.utils.six import b

import responses
from wagtail.wagtailcore.models import Site

from wagtaildocs_previews.models import (
    FilePreviewsSettings, PreviewableDocument
)


def setup_mock():
    def request_callback(request):
        payload = json.loads(request.body.decode('utf8'))
        body = {
            'id': '1',
            'status': 'pending',
            'thumbnails': None,
            'url': 'https://api.filepreviews.io/v2/previews/1/',
            'preview': None,
            'original_file': None,
            'user_data': payload['data']
        }

        headers = {
            'content-type': 'application/json',
            'location': body['url']
        }

        return (201, headers, json.dumps(body))

    responses.add_callback(
        responses.POST, 'https://api.filepreviews.io/v2/previews/',
        callback=request_callback,
        content_type='application/json',
    )


class TestPreviewableDocument(TestCase):
    def setUp(self):
        self.site = Site.objects.get(is_default_site=True)
        self.settings = FilePreviewsSettings.for_site(self.site)
        self.settings.api_key = 'DUMMY_API_KEY'
        self.settings.api_secret = 'DUMMY_API_SECRET'
        self.settings.save()

    @responses.activate
    def test_filepreviews_generate_when_creating_doc(self):
        setup_mock()

        PreviewableDocument.objects.create(
            title='Test document',
            file=ContentFile(b('Hello world'), 'test1.txt')
        )

        self.assertEqual(len(responses.calls), 1)

    @responses.activate
    def test_filepreviews_generate_when_updating_file(self):
        setup_mock()

        document = PreviewableDocument.objects.create(
            title='Test document',
            file=ContentFile(b('Hello world'), 'test1.txt')
        )

        document.file = ContentFile(b('Hello world'), 'test2.txt')
        document.save()

        self.assertEqual(len(responses.calls), 2)

    @responses.activate
    def test_filepreviews_doesnt_generate_if_settings_not_enabled(self):
        setup_mock()

        self.settings.api_key = ''
        self.settings.api_secret = ''
        self.settings.save()

        PreviewableDocument.objects.create(
            title='Test document',
            file=ContentFile(b('Hello world'), 'test1.txt')
        )

        self.assertEqual(len(responses.calls), 0)
