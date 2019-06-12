from django import forms
from .models import Post

class PostForm(forms.Form):
    industory = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "WEB制作会社"
        })
    )

    career = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "エンジニア"
        })
    )
    
    age = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "20代"
        })
    )

    contents = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "あなたのはたらくことば"
        })
    )
