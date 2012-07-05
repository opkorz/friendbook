from django.contrib.auth.models import User
from fbook.friend.models import UserLink
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello World')
def user(request):
    list_1 = User.objects.all()
    #return HttpResponse(list_1)    
    return render_to_response('user.html', {'list_1':list_1})
def follower(request, username):
    get_User= User.objects.get(username=username)
    list_1 = UserLink.objects.filter(to_user = get_User)
    list_2 = []
    for link in list_1:
        list_2.append(link.from_user)
    return render_to_response('follower.html', {'list_2':list_2})
def following(request, username):
    get_User= User.objects.get(username=username)
    list_1 = UserLink.objects.filter(from_user = get_User)
    list_2 = []
    for link in list_1:
        list_2.append(link.to_user)
    return render_to_response('following.html', {'list_2':list_2})
def profile(request, username):
    get_User = User.objects.get(username=username)
    return render_to_response('profile.html', {'user':get_User})
