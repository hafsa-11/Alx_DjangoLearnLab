from django import forms

class SearchForm(forms.Form):
    term = forms.CharField(max_length=100)

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
