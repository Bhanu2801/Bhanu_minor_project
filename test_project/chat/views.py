from django.shortcuts import render 
from django.contrib.auth import authenticate, logout, login 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse 
from test_project import settings 
from .models import Chat 

#import pdb;
 
# def Login(request): 
#     next = request.GET.get('next', 'chat/home/') 
#     if request.method is "POST": 
#         username = request.POST['username'] 
#         password = request.POST['password'] 
#         user = authenticate(username=username, password=password) 
 
 
#         if user is not None: 
#             if user.is_active: 
#                 login(request, user) 
#                 return HttpResponseRedirect(next) 
#             else: 
#                 return HttpResponse("Account is not active at the moment.") 
#         else: 
#             return HttpResponseRedirect(settings.LOGIN_URL) 
#     return render(request, "login.html", {'next': next}) 
 
 
# def Logout(request): 
#     logout(request) 
#     return HttpResponseRedirect('/login/') 
 
 
def Home(request): 
    c = Chat.objects.all() 
    return render(request, "chatpage.html", {'home': 'active', 'chat': c}) 
 
 
def Post(request):
    #pdb.set_trace()
    if request.method=="POST": 
        msg = request.POST.get('msgbox', None) 
        c = Chat(user=request.user, message=msg) 
        if msg != '': 
            c.save() 
        return JsonResponse({ 'msg': msg, 'user': c.user.username }) 
    else: 
        return HttpResponse('Request must be POST.') 
 
 
def Messages(request): 
    c = Chat.objects.all() 
    return render(request, 'messages.html', {'chat': c}) 

# Create your views here.
