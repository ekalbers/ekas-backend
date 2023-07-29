from django.http import JsonResponse


def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.csrf_token})

