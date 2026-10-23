from django.shortcuts import render

from .models import Event
# Create your views here.

def calendar_view(request):
    events = EVent.ohjects.all().order_by('date')
    return render(request, 'calendar.html', {'events': events})