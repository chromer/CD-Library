import datetime

from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Event


@login_required
def today(request):
    d = datetime.date.today()
    t = datetime.time(0, 0, 0)
    today = datetime.datetime.combine(d, t)
    events = Event.objects.filter(author=request.user).filter(
            timestamp__gt=today)
    context = {
            'events': events,
    }
    return render_to_response('diary/today.html', RequestContext(request, context))


@login_required
def add_event(request):
    pass
