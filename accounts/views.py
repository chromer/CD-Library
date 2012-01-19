from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


def login_user(request):
    msgs = []
    if request.method == 'POST':
        username = request.POST['username_in']
        password = request.POST['pwd_in']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin/')
            else:
                msgs.append('Your account is disabled. Please contact\
                        site admin to restart it.')
        else:
            msgs.append('Username and password didn\'t match.')
    context = {
            'msgs': msgs,
    }
    return render_to_response('login.html', RequestContext(request, context))


def signup(request):
    msgs = []
    if request.method == 'POST':
        username = request.POST['username_up']
        email = request.POST['email_up']
        password = request.POST['pwd_up']
        if username and password and email:
            if not User.objects.filter(username=username):
                try:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    return HttpResponseRedirect('/admin/')
                except:
                    msgs.append('Some error occured in createing the new user')
            else:
                msgs.append('Username already exists. Please try some other username.')
        else:
            msgs.append('Please submit a valid username, password and email.')
        context = {
                'msgs': msgs,
        }
        return render_to_response('login.html',
                RequestContext(request, context))
    else:
        raise Http404
