from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput
from django.contrib.auth.models import User

from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        help_texts = {
            'username' : None,
        }
        widgets = {
            'password' : PasswordInput(),
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username' : 'Enter Username',
            'password' : 'Enter Password'
        }
        help_texts = {
            'username' : None,
        }
        widgets = {
            'password' : PasswordInput(),
        }
