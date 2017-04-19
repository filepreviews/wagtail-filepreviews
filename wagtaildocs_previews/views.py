import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import PreviewableDocument


@csrf_exempt
def filepreviews_webhook(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf8'))
        user_data = body.get('user_data', {})
        document_id = user_data.get('document_id')

        try:
            document = PreviewableDocument.objects.get(pk=document_id)
            document.preview_data = body
            document.save()

            return JsonResponse({
                'success': True
            }, status=200)

        except PreviewableDocument.DoesNotExist:
            pass

    return JsonResponse({
        'success': False
    }, status=400)
