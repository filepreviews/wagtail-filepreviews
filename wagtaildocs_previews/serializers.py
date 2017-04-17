from rest_framework.serializers import JSONField
from wagtail.wagtaildocs.api.v2 import serializers


class DocumentSerializer(serializers.DocumentSerializer):
    preview_data = JSONField(read_only=True)
