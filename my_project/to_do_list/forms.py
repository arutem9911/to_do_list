from django import forms
from django.forms import ValidationError
from .models import Tasks, Project, Status, Type
import datetime


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('start_date', 'end_date', 'title', 'description')
        widgets = {
            'start_date': forms.DateInput(),
            'end_date': forms.DateInput(),
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

    def clean_short_description(self):
        title = self.cleaned_data.get('title')
        if len(title) > 100:
            raise ValidationError(
                'This field should be no longer than %(length)d symbols',
                code='too_long',
                params={'length': 100}
            )
        return title

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data.get('title')) > len(cleaned_data.get('description')):
            raise ValidationError('The description should be longer than the title')
        return cleaned_data


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('short_description', 'description', 'status', 'type', 'project')
        widgets = {
            'short_description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'status': forms.Select(attrs={'class': 'form-select mb-3'}),
            'type': forms.Select(attrs={'class': 'form-select mb-3'}),
            'project': forms.Select(attrs={'class': 'form-select mb-3'}),
        }

    def clean_short_description(self):
        short_description = self.cleaned_data.get('short_description')
        if len(short_description) > 100:
            raise ValidationError(
                'This field should be no longer than %(length)d symbols',
                code='too_long',
                params={'length': 100}
            )
        return short_description

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data.get('short_description')) > len(cleaned_data.get('description')):
            raise ValidationError('The description should be longer than the short description')

        return cleaned_data


class ProjectTaskModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('short_description', 'description', 'status', 'type')
        widgets = {
            'short_description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'status': forms.Select(attrs={'class': 'form-select mb-3'}),
            'type': forms.Select(attrs={'class': 'form-select mb-3'}),
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label='Find'
    )
