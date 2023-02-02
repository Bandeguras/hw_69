from django.urls import path, include

from api_v1.views import echo_view, get_token_view
app_name = 'api_v1'

urlpatterns = [
    path('<str:method>/', echo_view),
    path('get_token/', get_token_view),
]