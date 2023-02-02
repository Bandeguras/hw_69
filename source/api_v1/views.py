from functools import reduce
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
import json


def echo_view(request, *args, **kwargs):
    user_value = {}

    if request.body:
        user_value = json.loads(request.body)

    answer = {}
    try:
        if kwargs['method'] == 'add':
            answer['answer'] = sum(user_value.values())

        elif kwargs['method'] == 'subtract':
            answer['answer'] = reduce(lambda x, y:x-y, user_value.values())

        elif kwargs['method'] == 'multiply':
            answer['answer'] = reduce(lambda x, y:x*y, user_value.values())

        elif kwargs['method'] == 'divide':
            try:
                answer['answer'] = reduce(lambda x, y:x/y, user_value.values())
            except ZeroDivisionError:
                answer['answer'] = "Division by zero!"

    except TypeError:
        answer['answer'] = "Value must be integer"

    response_data_json = json.dumps(answer)
    response = HttpResponse(response_data_json)
    response['Content-Type'] = 'application/json'
    return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
