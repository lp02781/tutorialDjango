from django.shortcuts import render

def index(request):
	context = {
		'title':'open class',
		'contrib':'whatever',
	}
	return render(request, 'index.html', context)
