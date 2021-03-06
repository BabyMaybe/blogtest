from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput, DateInput, NumberInput, HiddenInput, TextInput
from django.contrib.auth.models import User

from .models import Post, Comment, UserProfile, BugReport

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'rich_content']
        labels  = {
            'title'   : ': Title ',
            'rich_content' : ': Post Content '
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['display_author', 'content', ]

        widgets = {
        'content' : forms.Textarea(attrs = {'id' : 'new-comment',
                                            'placeholder': 'THIS SOME WILD SHIT'}),
        'display_author' : forms.TextInput(attrs = {'id' : 'new-comment-author',
                                                    'value' : 'anonymous coward'}),
        }

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']
        help_texts = {
            'username' : None,
        }
        labels = {
            'username'  : ': Username ',
            'password'  : ': Password ',
            'email'     : ': Email Address ',
            'first_name': ': First Name ',
            'last_name' : ': Last Name ',
        }
        widgets = {
            'password' : PasswordInput(),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age','birthday','color']
        widgets = {
            'birthday' : DateInput(),
            'age' : NumberInput(),

        }
        labels = {
            'color' : ': Favourite Colour ',
            'birthday' : ': Birthday mm/dd/yy ',
            'age'      : ': Age ',
        }

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username' : ': Enter Username ',
            'password' : ': Enter Password '
        }
        help_texts = {
            'username' : None,
        }
        widgets = {
            'password' : PasswordInput(),
        }

class BugForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['os', 'browser', 'feature', 'bug', 'steps']
        labels = {
            'os' : 'Operating System',
            'browser' : 'Web Browser',
            'feature' : 'Feature Request?',
            'bug' : 'What did you break/What feature is missing?',
            'steps' : 'What steps are needed to reproduce this issue?'
        }

class EmailTestForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    # class Meta:
    #     fields ['name']
    #     widgets = {
    #         'name' : TextInput(),
    #     }
