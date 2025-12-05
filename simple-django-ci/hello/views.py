from django.http import JsonResponse, HttpResponse


def index(request):
    # simple JSON API
    if request.headers.get('Accept') == 'application/json' or request.GET.get('format') == 'json':
        return JsonResponse({'message': 'Hello, world!', 'status': 'ok'})

    # simple HTML fallback
    return HttpResponse('<h1>Hello, world!</h1><p>Visit <a href="/?format=json">JSON</a></p>')
