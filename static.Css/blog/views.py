from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'Blog byCode.id',
        'subtitle':'Welcome to byCode.id blog ',
        'banner':'blog/img/banner_blog.png',
        'app_css':'blog/css/styles.css'
    }
    return render(request,'index.html',context)