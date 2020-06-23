from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        required=False)
    url_file = forms.URLField(
        label='input url of picture',
        required=False)
