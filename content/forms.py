from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput, DateInput, NumberInput
from django.contrib.auth.models import User

from .models import Post, Comment, UserProfile

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

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age','birthday','addr_street','addr_city','addr_state','addr_zip','color']
        widgets = {
            'birthday' : DateInput(),
            'age' : NumberInput(),

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
