import datetime

from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse
from models import Event
from forms import EventForm


@login_required
def today(request):
    form = EventForm()
    d = datetime.date.today()
    t = datetime.time(0, 0, 0)
    today = datetime.datetime.combine(d, t)
    events = Event.objects.filter(author=request.user).filter(
            timestamp__gt=today)
    context = {
            'form': form,
            'events': events,
    }
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            try:
                event.save()
                context['msgs'] = ['Event added successfully.',]
            except:
                context['msgs'] = ['Some error occured. Please enter valid data.',]
                context['form'] = form
        else:
            context['msgs'] = ['Error: You must enter a title.',]
            context['form'] = form
    return render_to_response('diary/today.html', RequestContext(request, context))


@login_required
def plus_or_minus(request):
    if request.is_ajax():
        id = request.POST['id']
        event = get_object_or_404(Event, pk=id)
        if request.user in event.ups.all():
            event.ups.remove(request.user)
            msg = '+ '+str(event.ups.count())
        else:
            event.ups.add(request.user)
            msg = '&minus; '+str(event.ups.count())
        return HttpResponse(msg)
    else:
        raise Http404
