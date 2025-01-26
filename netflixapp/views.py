from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return render(request, 'netflixapp/index.html') 
def login(request):
    return render(request, 'accounts/login.html')
