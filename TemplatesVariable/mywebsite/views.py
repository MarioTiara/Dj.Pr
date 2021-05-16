from django.shortcuts import render 

def index (request):
    context={
        'title':'Seever Web',
        'contrib':'Mario Tiara '
    }
    return render (request,'index.html',context)