from django.shortcuts import render

def index(request):
    context={
      'judul': 'ByCode.id',
      'subjudul':'Welcome',
      'nav':[
        ['/','Home'],
        ['blog/','Blog'],
        ['product/','Product'],
      ]
    }

    return render(request,'index.html',context)