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
    user_avatar = models.ImageField(upload_to ='uploads/')
    #user_avatar = models.CharField(max_length=100)
    visitor_status = models.BooleanField(default=False)
    collaborator = models.BooleanField(default=False)