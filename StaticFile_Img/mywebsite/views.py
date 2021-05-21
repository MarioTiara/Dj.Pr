from django.http import request
from django.shortcuts import render

def index (request):
    context={

        'title':'byCode.id',
        'subtitle':'Welcome to our Website',
        'banner':'img/banner_home.png'
        
    }
    return  render(request,'index.html',context)
    
