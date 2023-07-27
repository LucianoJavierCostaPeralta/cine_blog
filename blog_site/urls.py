from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #General
    path('', views.home, name="home"),
    path('nosotros/', views.about, name="nosostros"),

    # Register & login
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),

    #articules
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)