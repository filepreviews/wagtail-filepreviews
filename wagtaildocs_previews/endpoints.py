from wagtail.wagtaildocs.api.v2 import endpoints

from .serializers import DocumentSerializer


class DocumentsAPIEndpoint(endpoints.DocumentsAPIEndpoint):
    base_serializer_class = DocumentSerializer
    body_fields = endpoints.DocumentsAPIEndpoint.body_fields + ['preview_data']
