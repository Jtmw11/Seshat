from django import forms

class DocumentForm(forms.Form):
    #title =
    image = forms.FileField(
        label='Select a file'
    )