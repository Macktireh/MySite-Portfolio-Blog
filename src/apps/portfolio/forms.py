from .models import Competence, Project, Category, Contact
from django import forms
from django.forms import fields
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, min_length=3, required=True, widget=forms.TextInput(attrs={'id': 'name', 'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'autocomplete': 'off'}))
    subject = forms.CharField(max_length=128, required=False, widget=forms.TextInput(attrs={'id': 'subject', 'autocomplete': 'off'}))
    message = forms.CharField(max_length=10000, min_length=10, required=True, widget=forms.Textarea(attrs={'id': 'message', 'class': 'form-control', 'autocomplete': 'off'}))
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
    # def clean_name(self, *args, **kwargs):
    #     name = self.cleaned_data.get('name')
    #     if name is not None:
    #         raise forms.ValidationError("le nom ne doit pas être vide et compris entre 3 et 50 caractères")
    #     # elif not 'mack' in name:
    #     #     raise forms.ValidationError("le nom ne doit contenir mack")
    #     else:
    #         return name
    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if email is not None:
    #         raise forms.ValidationError("le nom ne doit pas être vide")
    #     else:
    #         return email
    
    # def clean_message(self, *args, **kwargs):
    #     message = self.cleaned_data.get('message')
    #     if message is not None:
    #         raise forms.ValidationError("le nom ne doit pas être vide et compris entre 10 et 10000 caractères")
    #     else:
    #         return message
    

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'id':'name','autocomplete': 'off'})
    #     self.fields['email'].widget.attrs.update({'id':'email','autocomplete': 'off'})
    #     self.fields['message'].widget.attrs.update({'id':'message','autocomplete': 'off'})