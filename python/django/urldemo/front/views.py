from django.shortcuts import render
from django.shortcuts import redirect,reverse
# Create your views here.
from django.http import HttpResponse
def index(request):
    username=request.GET.get('username')
    if username:
        return HttpResponse('front首页')
    else:
        return redirect(reverse('front:login'))

def login(request):
    return HttpResponse('front登录')