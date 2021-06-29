from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(label="Titulo", max_length=15, required=True,
        validators=[
            validators.MinLengthValidator(4, 'Muy corto'),
            validators.RegexValidator('^[A-Za-z0-9]*$', "No cumple con RegEx")
        ]
    )
    content = forms.CharField(label="Contenido", widget=forms.Textarea)
    public = forms.TypedChoiceField(choices=[(1, 'Sí'), (0, 'No')])