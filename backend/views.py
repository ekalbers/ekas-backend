from django.middleware.csrf import get_token
from django.http import JsonResponse


def get_csrf_token(request):
    # csrf_token = get_token(request)
    print(request)
    return JsonResponse({
        # 'csrfToken': request.COOKIES['csrftoken'],
        'request': request
    })
