from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'About',
        'contrib':'CONTRIBUTORS'
    }
    return render(request,'about/index.html',context)

def Mario(request):
    context={
        'title':'About Mario',
        'contrib':'Mario Tiara Pratama (Kaur)'
    }
    return render(request,'about/index.html',context)

def Aji(request):
    context={
        'title':'About Aji',
        'contrib':'Aji Arya Dewangga (Kediri)'
    }
    return render(request,'about/index.html',context)

def Dery (request):
    context={
        'title':'About Dery',
        'contrib':'Dery Ardiansyah (Bengkulu)'
    }
    return render(request,'about/index.html',context)

def Ganesh (request):
    context={
        'title':'About ',
        'contrib':'Ganesha Ali Ranan (Kedurang)'
    }
    return render(request,'about/index.html',context)
