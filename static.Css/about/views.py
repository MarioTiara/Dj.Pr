from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'About byCode.id',
        'subtitle':'Its about byCode.id',
        'banner':'about/img/banner_about.png',
        'app_css':'about/css/styles.css',
    }
    return render(request,'index.html',context)