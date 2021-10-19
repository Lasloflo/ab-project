from django import forms
from django.forms import TextInput, Textarea
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={'class': "form-control", 'id': "name", 'placeholder': "Your NameForm"}))
    email = forms.CharField(required=False, max_length=250, widget=TextInput(attrs={'class': "form-control", 'id': "email", 'placeholder': "Your EmailForm"}))
    phone = PhoneNumberField(required=True, widget=TextInput(attrs={'class': 'form-control', 'id':'phone', 'placeholder': 'PhoneForm'}))
    subject = forms.CharField(required=False, widget=TextInput(attrs={'class': "form-control", 'id':"phone", 'placeholder': "SubjectForm"}))
    message = forms.CharField(required=True, widget=Textarea(attrs={'class': "form-control", 'id':"message", 'placeholder': "MessageForm"}))
    required_css_class = "error_input"
    error_css_class = "error_input"
