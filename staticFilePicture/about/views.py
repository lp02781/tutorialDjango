from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'judul':'about',
        'subjudul':'tentang'
    }
    return render(request, 'about/index.html', context)