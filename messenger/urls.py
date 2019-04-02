from django.urls import path, re_path
from messenger import views
from .views import room

app_name = 'messenger'

urlpatterns = [
    path('', views.HomeView.as_view()),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]