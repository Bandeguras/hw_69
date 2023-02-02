from django.urls import path, include

from api_v1.views import echo_view
app_name = 'api_v1'

# article_url = [
#     path('', article_view)
# ]

urlpatterns = [
    path('echo/', echo_view),
]