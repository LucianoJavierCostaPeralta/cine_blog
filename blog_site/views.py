from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    articles = Article.objects.all()    

    return render(request, 'home.html' , {
        'articles': articles})

def about(request):
    return render(request, 'about.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')
