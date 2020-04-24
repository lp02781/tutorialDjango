from django.shortcuts import render

def index(request):
    context = {
        'judul':'Open class',
        'subjudul':'welcome',
        'banner':'img/home.jpg'
    }
    return render(request, 'index.html', context)