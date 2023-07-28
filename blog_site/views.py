from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Article
from .forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.username_validation()
            form.email_validation()

            # Validate the status fields
            form.status_validation()

            # Validate the password fields
            form.password_validation()

            # Validate the user avatar field
            form.user_avatar_validation()

            # Save the form data to the database
            form.save_to_database()

                # Redirect to a success page after successful registration
            return HttpResponse('user registration successfull')
            """except:
                # If any validation error occurs, display the form with the error
                return render(request, 'signup.html', {'registration_form': RegistrationForm})"""
    else:
        # Display an empty registration form for GET requests
        form = RegistrationForm()

    return render(request, 'signup.html', {'registration_form': RegistrationForm})

  

def signin(request):
    return render(request, 'signin.html')


def articles(request):
    articles = Article.objects.all()

    return render(request, 'articles.html' , {
        'articles': articles})

def article(request, article_id):
    article = get_object_or_404(Article, article_id=article_id)

    return render(request, 'article.html', {'article': article})

