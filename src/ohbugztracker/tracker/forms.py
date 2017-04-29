from django import forms
from .models import Project


class ProjectForm(forms.Form):
    title = forms.CharField(label='Enter Title', help_text='Custom CMS',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'cols': "80", 'rows': "10", 'class': 'form-control'}))
