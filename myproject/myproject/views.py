from django.http import HttpResponse

def home(rquest):
    return HttpResponse("Welcome to the home page")

def home(request):
    return HttpResponse("Hello, World!  dota ki First project.")

def about(request):
    return HttpResponse("My About Page. is this working ?")

 
    