from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Helllo world, this is poll index')