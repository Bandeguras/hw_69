from django.http import HttpResponse
from datetime import datetime


def echo_view(request, *args, **kwargs):
    response_data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method
    }
    response = HttpResponse(response_data)
    return response