from django import forms

class add_to_cart(forms.Form):
    quantity=forms.IntegerField()