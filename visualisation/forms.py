from django import forms

class YourCSVUploadForm(forms.Form):
    file = forms.FileField()
