from django.shortcuts import render
def index(request):
	context={
		'title':'open class',
		'subtitle':'hell',
		'nav':[
			['/' , 'Home'],
			['/blog', 'Blog'],
			['/about', 'About'],
			['/contact', 'contact']
		]
	}
	return render(request,'index.html', context)
