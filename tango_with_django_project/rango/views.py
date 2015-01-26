from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return HttpResponse( 'Rango says: Hello world!')

def about(request):
	return HttpResponse( "Rango says this is the about page, this tutorial has been put together by Alexandra Russell, 2092971R")

