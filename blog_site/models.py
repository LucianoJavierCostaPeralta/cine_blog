from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=50)
    online_status = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    user_avatar = models.ImageField(upload_to ='uploads/user_avatars/')
    visitor_status = models.BooleanField(default=False)
    collaborator_status = models.BooleanField(default=False)

class Article(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    article_ownership = models.ForeignKey(User, on_delete=models.CASCADE)
    article_creation_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True, default='')
    tags = models.CharField(max_length=200)
    content = models.TextField()
    last_edit = models.DateField(auto_now=True)
    upload_status = models.BooleanField(default=False)
    lmage = models.ImageField(upload_to ='uploads/assets/')

class Comments(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    comment_ownership = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_creation_date = models.DateField(auto_now_add=True, verbose_name="creation_date")
    content = models.TextField()
    last_edit = models.DateField(auto_now=True)
    upload_status = models.BooleanField(default=False)