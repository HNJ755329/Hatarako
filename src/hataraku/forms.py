from django import forms
from .models import Post
from .models import Color
from colorfield.fields import ColorField

class PostForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = ('contents', 'industory', 'career', 'age', 'color')
        widgets = {
            'contents': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "あなたのはたらくことば"
                }),
            'industory' : forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "WEB制作会社"
            }),
            'career':forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "エンジニア"
            }),
            'age' : forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "20代"
            }),
            'color' : forms.TextInput(attrs={
                'type': 'color',
                'value':"#333333",
                'list':"colors",
            }),
        }

class _PostForm(forms.Form):
    contents = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "あなたのはたらくことば"
        })
    )

    industory = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "WEB制作会社"
        })
    )

    career = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "エンジニア"
        })
    )
    
    age = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "20代"
        })
    )

    #color = forms.CharField(widget=ColorPickerWidget)
    #color = forms.ModelChoiceField(queryset=Color.objects.all())
