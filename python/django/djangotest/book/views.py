from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def book(request):
    return HttpResponse('书籍首页')

def book_detail(request,book_id,category_id):
    text='您获取的图书id是:%s---%s' % (book_id,category_id)
    return HttpResponse(text)

def author_detail(request):
  author_id=request.GET.get('id')
  test='作者的id是:%s'%author_id
  return HttpResponse(test)

