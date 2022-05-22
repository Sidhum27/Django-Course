
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
 return HttpResponse("hello")
 

def about(request):
   data={
      'title':'my page',
      'clist':['php','pyton','js']
   }
   return  render(request,'index.html',data)

def aboutDetails(request,id):
    return HttpResponse("this is aboutDetilas "+id)

