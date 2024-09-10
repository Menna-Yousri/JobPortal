from django import forms

from .models import Apply , Job

from django.forms import Textarea




class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name' ,'email','webiste','cv','cover_letter']
        name = forms.CharField(
            label='Your name', 
            max_length=100,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'})
        )
        email = forms.EmailField(
            label='Email',
            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        )
        website = forms.URLField(
            label='Website/Portfolio link',
            required=False,
            widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Website/Portfolio link'})
        )
        cv = forms.FileField(
            label='Upload CV',
            widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        )
        cover_letter = forms.CharField(
            label='Coverletter',
            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Coverletter'})
        )



class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','slug')