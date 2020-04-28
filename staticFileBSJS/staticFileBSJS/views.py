from django.shortcuts import render

def index(request):
    context={
        'title':'open class',
        'heading':'Welcome',
        'subheading':'welcome in open class',
    }
    return render(request, 'index.html', context)