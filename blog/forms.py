from django import forms
from .category import Category

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'custom-title-form form-control'
            }),
            'text': forms.Textarea(attrs={
                'class': 'custom-text-form form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'custom-category-select form-control'
            })
        }