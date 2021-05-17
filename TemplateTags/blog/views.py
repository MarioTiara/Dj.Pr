from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    context={
        'judul': 'ByCode',
        'subjudul':'Blog',
        'nav':[
            ['/','Home'],
            ['/blog/stories','Stories'],
            ['/blog/news','News'],
        ]
    }
    return render (request,'index.html',context)

def stories(request):
    return HttpResponse("<h1> Stories </h1>")

def news(request):
    return HttpResponse("<h1> News </h1>")