from .models import Competence, Project, Category, Contact
from django import forms
from django.forms import fields
from ckeditor.widgets import CKEditorWidget

class ContactForm(forms.ModelForm):
	# name = forms.CharField(
    #     max_length=30, widget=forms.TextInput(
    #         attrs={'id': 'name',
    #                'autocomplete': 'off'}
    #     ))
	# email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #                'autocomplete': 'off'}
    #     ))
	# message = forms.CharField(widget=forms.Textarea(attrs={'id':'message'}))
    # message = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'id':'name','autocomplete': 'off'})
        self.fields['email'].widget.attrs.update({'id':'email','autocomplete': 'off'})
        self.fields['message'].widget.attrs.update({'id':'message','autocomplete': 'off'})
  
        