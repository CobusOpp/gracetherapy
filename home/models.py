from django.db import models
from django.forms import ModelForm

from phonenumber_field.modelfields import PhoneNumberField

class Contact(models.Model):
        first_name = models.CharField(max_length=150, null=True)
        last_name = models.CharField(max_length=150, null=True)
        cell_number = PhoneNumberField(null=True)
        email_address = models.EmailField(max_length=150, null=True)
        child_name = models.CharField(max_length=150, null=True)
        child_age = models.CharField(max_length=5, null=True)
        school_name = models.CharField(max_length=150, null=True)
        child_grade = models.CharField(max_length=5, null=True)
        preferred_date = models.DateField(null=True)
        time_choices = models.CharField(max_length=5, null=True)
        contact_choices = models.CharField(max_length=5, null=True)

        def __str__(self):
            return self.name

class ContactList(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, default=None, name='Bussiness_name')
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, null=True, blank=True)
    tel_num = PhoneNumberField(null=True)
    description = models.CharField(max_length=250)
    url = models.URLField(blank = True)

    def __str__(self):
        return self.Bussiness_name