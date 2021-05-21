from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'About byCode.id',
        'subtitle':'Its about byCode.id',
        'banner':'about/img/banner_about.png',
    }
    return render(request,'index.html',context)