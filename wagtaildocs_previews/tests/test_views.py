import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from wagtaildocs_previews.models import PreviewableDocument


class TestWebhookView(TestCase):
    def setUp(self):
        self.url = reverse('filepreviews_webhook')
        self.document = PreviewableDocument.objects.create(
            title='Test document'
        )

    def test_post_returns_success(self):
        post_data = {
            'user_data': {
                'document_id': self.document.id
            }
        }

        response = self.client.post(
            self.url, json.dumps(post_data), content_type='application/json'
        )

        self.assertEqual(response.content.decode('utf8'), '{"success": true}')

    def test_post_updates_document(self):
        post_data = {
            'user_data': {
                'document_id': self.document.id
            }
        }

        self.client.post(
            self.url, json.dumps(post_data), content_type='application/json'
        )

        document = PreviewableDocument.objects.get(pk=self.document.pk)

        self.assertEqual(document.preview_data, post_data)
