from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MouseEvent
from django.utils.dateparse import parse_datetime
import json

def track_mouse_page(request):
    return render(request, 'mouseinput/track-mouse.html')

@csrf_exempt
def track_mouse(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        for event_data in data:
            MouseEvent.objects.create(
                event_type=event_data['type'],
                x=event_data['x'],
                y=event_data['y'],
                timestamp=parse_datetime(event_data['timestamp'])
            )
        
        return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse({'status': 'error'}, status=400)

def view_mouse_events(request):
    events = MouseEvent.objects.all().order_by('-timestamp')[:100]  
    return render(request, 'mouseinput/view_events.html', {'events': events})