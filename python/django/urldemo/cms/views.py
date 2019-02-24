from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse('CMS首页')
def login(request):
    return HttpResponse('CMS登录')