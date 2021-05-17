from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'ByCode',
        'subjdul':'Product',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/product/','Product'],

        ]
    }
    return render(request,'index.html',context)