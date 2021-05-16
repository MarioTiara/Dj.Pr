from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Blog',
        'contrib':'Dery Ardyan '
    }

    return render(request,'blog/index.html',context)

def stories(request):
    context={
        'title':'Stories',
        'contrib':'Aji arya'
    }

    return render(request,'blog/index.html',context)

def news(request):
    context={
        'title':'News',
        'contrib':'Ganesha ali '
    }

    return render(request,'blog/index.html',context)