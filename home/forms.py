from django import forms
from django.forms import ModelForm
from .models import Contact
from django.contrib.admin.widgets import AdminDateWidget

TIME_CHOICES = [
    ('13:30 - 14:15','13:30 - 14:15'),
    ('14:30 - 15:15','14:30 - 15:15'),
    ('15:30 - 16:15','15:30 - 16:15'),
    ('16:30 - 17:15','16:30 - 17:15')
    ]

CONTACT_CHOICES = [
    ('Email','Email'),
    ('Phone call','Phone call'),
    ('WhatsApp','WhatsApp')
    ]

class ContactForm(forms.Form):
    first_name = forms.CharField( label="First Name")
    last_name = forms.CharField(label="Last Name")
    cell_number = forms.CharField(label="Cell Number")
    email_address = forms.EmailField(label="Email Address")
    child_name = forms.CharField(label="Child Name")
    child_age = forms.CharField(label="Child Age")
    school_name = forms.CharField(label="School Name")
    child_grade = forms.CharField(label="Child Grade")
    preferred_date = forms.DateField(widget=AdminDateWidget())
    time_choices = forms.CharField(label="Please select a time: ", widget=forms.RadioSelect(choices=TIME_CHOICES))
    contact_choices = forms.CharField(label="Contact Preferences", widget=forms.RadioSelect(choices=CONTACT_CHOICES))
