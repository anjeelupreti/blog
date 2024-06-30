from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude =['add_date','author']

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude =['add_date','author']
    