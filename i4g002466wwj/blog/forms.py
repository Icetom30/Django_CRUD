from django import forms
from .models import BlogApp

class Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "author" 
        ]