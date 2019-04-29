from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
def index(request):
    #html = render_to_string("index.html")
# Create your views here.
    #return HttpResponse(html)
    a = {
        'test1':'jhc',
    }
    return render(request,'index.html',context=a)