from functools import reduce
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from django.views.generic import TemplateView


def echo_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            user_value = json.loads(request.body)
            answer = {}
            try:
                for key in user_value:
                    user_value[key] = int(user_value[key])

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

            except ValueError:
                answer['answer'] = "Value must be integer"

            response_data_json = json.dumps(answer)
            response = HttpResponse(response_data_json)
            response['Content-Type'] = 'application/json'
            return response
    else:
        response = JsonResponse({'error': 'No data provided!'})
        response.status_code = 400
        return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class AboutView(TemplateView):
    template_name = "index.html"