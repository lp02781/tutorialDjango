from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'blog',
		'contrib':'haha',
	}
	return render(request, 'blog/index.html',context)

def news(request):
	context = {
		'title':'news',
		'contrib':'hihi',
	}
	return render(request, 'blog/index.html',context)
	
def story(request):
	context = {
		'title':'story',
		'contrib':'hehe',
	}
	return render(request, 'blog/index.html',context)
