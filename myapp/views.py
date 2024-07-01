from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h2>hola mundo</h2>')

def about(request):
    return HttpResponse('Pendejo')