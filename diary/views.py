import datetime

from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from models import Event
from forms import EventForm

def get_begining(date):
    d = date.date()
    t = datetime.time(0, 0, 0)
    return datetime.datetime.combine(d, t)


@login_required
def today(request):
    form = EventForm()
    today = get_begining(datetime.datetime.now())
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
                context['msgs'] = ['Some error occured. Please enter \
                        valid data.',]
                context['form'] = form
        else:
            context['msgs'] = ['Error: You must enter a title.',]
            context['form'] = form
    return render_to_response('diary/today.html',
            RequestContext(request, context))


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

@login_required
def search_events(request):
    if request.method == 'POST':
        q = request.POST['q']
        q = q.strip()
        if q:
            events = Event.objects.filter(author=request.user).filter(
                    Q(title__icontains=q) |
                    Q(description__icontains=q)).order_by('-timestamp')[:15]
            context = {
                    'events': events,
            }
            return render_to_response('diary/search.html', RequestContext(request, context))
        else:
            return HttpResponseRedirect('/diary/today')
    else:
        raise Http404
