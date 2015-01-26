from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return HttpResponse( 'Rango says: Hello world!')

def about(request):
	return HttpResponse( "Rango sayd this is the about page" )

