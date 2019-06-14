from django import forms
from .models import Post
from .models import Color
from colorfield.fields import ColorField

class PostForm(forms.Form):
    contents = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "あなたのはたらくことば"
        })
    )

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

    color = ColorField(default='#000000')
    #color = forms.ModelChoiceField(queryset=Color.objects.all())

