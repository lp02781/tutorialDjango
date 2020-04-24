from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Blog',
        'subjudul' : 'this is blog',
        'banner' : 'blog/img/blog.jpg',
        'app_css': 'blog/css/styles.css'
    }
    return render(request, 'index.html', context)