from django import forms
from django.forms import ModelForm
from owner.models import Books
class BookForm(ModelForm):
    class Meta:
        model=Books

        exclude=("active_status",)
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
