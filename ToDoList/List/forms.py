from dataclasses import fields
from django import forms
from .models import Item


class ListForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item", "status"]
