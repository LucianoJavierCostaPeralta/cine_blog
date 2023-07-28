from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
import os
from .models import User
from django.core.files import File

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    user_email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    #visitor status as collaborator or visitor
    visitor_status = forms.BooleanField(required=False)
    collaborator_status = forms.BooleanField(required=False)

    user_avatar = forms.ImageField(required=False)

    def username_validation(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken. Please choose a different one.")
        else:
            return username

    def email_validation(self):
        email = self.cleaned_data.get('user_email')

        if User.objects.filter(user_email=email).exists():
            raise ValidationError("This email is already registered. Please use a different one.")
        else:
            return email

    def status_validation(self):
        cleaned_data = super().clean()
        visitor_value = cleaned_data.get('visitor_status')
        collaborator_value = cleaned_data.get('collaborator_status')

        if (visitor_value == False and collaborator_value == False):
            raise forms.ValidationError("Please choose at least one option.")
        elif (visitor_value == True and collaborator_value == True):
            raise forms.ValidationError("Please select only one option.")
        else:
            return cleaned_data
        
    def password_validation(self):
        cleaned_data = super().clean()
        password1_value = cleaned_data.get('password1')
        password2_value = cleaned_data.get('password2')

        if password1_value != password2_value:
            raise forms.ValidationError("Passwords do not match.")
        else:
            return cleaned_data
        
    def user_avatar_validation(self):
        user_avatar = self.cleaned_data.get('user_avatar')

        if user_avatar is None:
            default_user_avatar = os.path.join(settings.STATIC_URL, "images/default-profile.jpg")
            user_avatar = default_user_avatar
            self.cleaned_data['user_avatar'] = user_avatar
    
        return user_avatar
        

    def save_to_database(self):
        cleaned_data = self.cleaned_data
        user_avatar = cleaned_data.get('user_avatar')
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        user_email = cleaned_data.get('user_email')
        visitor_status = cleaned_data.get('visitor_status')
        collaborator_status = cleaned_data.get('collaborator_status')

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            user_email=user_email,
            user_password=self.cleaned_data['password1'],
            user_avatar = user_avatar,
            visitor_status=visitor_status,
            collaborator_status=collaborator_status
        )

        user.save()
        
