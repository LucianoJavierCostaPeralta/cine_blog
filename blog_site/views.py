from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')


def articles(request):
    articles = Article.objects.all()

    return render(request, 'articles.html' , {
        'articles': articles})

def article(request, article_id):
    article = get_object_or_404(Article, article_id=article_id)

    return render(request, 'article.html', {'article': article})

