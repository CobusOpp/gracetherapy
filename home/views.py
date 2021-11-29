from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .models import ContactList


def home(request):
    return render(request, "home.html", {})

def contactView(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            body = {
                'first_name':request.POST.get('first_name'),
                'last_name':request.POST.get('last_name'),
                'cell_number':request.POST.get('cell_number'),
                'email_address':request.POST.get('email_address'),
                'child_name':request.POST.get('child_name'),
                'child_age':request.POST.get('child_age'),
                'school_name':request.POST.get('school_name'),
                'child_grade':request.POST.get('child_grade'),
                'preferred_date':request.POST.get('preferred_date'),
                'preferred_time':form.cleaned_data.get('time_choices'),
                'preferred_contact':form.cleaned_data.get('contact_choices'),
            }

            name = body['first_name']
            surname =body['last_name']

            subject = 'Booking Request for ' + name + ' ' + surname

            template = get_template('email.txt')

            message = template.render(body)

            try:
                send_mail(subject,
                  message, 'tcobus308@gmail.com', ['cobusopp.test1@gmail.com'], fail_silently=False)
                messages.success(request, 'Thank you for enquiry. We will contact you soon to confirm your booking.')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def terms(request):
    return render(request, "terms.html", {})

def privacy(request):
    return render(request, "privacy.html", {})

def list(request):
    contacts = ContactList.objects.all()
    return render(request, 'list.html', {'contacts': contacts})