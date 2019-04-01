from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


# chat/views.py
def index(request):
    return render(request, 'messenger/index.html', {})


def room(request, room_name):
    return render(request, 'messenger/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
