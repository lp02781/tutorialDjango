from django.http import HttpResponse

def index(request):
	tittle = "<h1> this is hell</h1>"
	subtittle = "<h2> welcome in hell</h2>"
	output = tittle+subtittle;
	
	return HttpResponse(output)
def about(request):
	return HttpResponse("<h1> this is about hell</h1>")
