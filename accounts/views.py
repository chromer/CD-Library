from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


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



