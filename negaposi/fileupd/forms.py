from django import forms
from django.core.validators import FileExtensionValidator


class PostDataForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content_message = forms.CharField(widget=forms.Textarea)
    data_file = forms.FileField(
        validators=[FileExtensionValidator(['txt', 'csv'])]
    )


"""
class Form(forms.ModelForm):
    class Meta:
        model = ExperimentResult
        fields = ("title", "comment",)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'text_area'}),
            'comment' : forms.TextInput(attrs={'class':'text_area'})
        }
"""
