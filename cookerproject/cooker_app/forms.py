from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    query = forms.CharField()

from .models import Comment

class CommentForm(forms.Form):
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )

class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')