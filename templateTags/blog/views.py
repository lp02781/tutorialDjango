from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title':'open class',
		'subtitle':'blog',
		'nav':[
			['/' , 'Home'],
			['/blog/stroy', 'story'],
			['/blog/news', 'News'],
		]
	}
	return render(request, 'index.html', context)
