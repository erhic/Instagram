from django import forms
from .models import Post,Comments
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field


class PostForm(forms.ModelForm):
    helper=FormHelper()
    helper.form_method='POST'
    helper.add_input(Submit('Post','Post',css_class='btn-primary'))
    
    class Meta:
        model=Post
        fields=[
            'image',
            'image_caption'
        ]
        
