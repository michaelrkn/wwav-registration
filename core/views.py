from django.shortcuts import render, redirect

# Create your views here.
from core.forms import RegisterForm, MailForm
from core.models import Zip

from django.urls import reverse


def index(request):
    context = {}
    return render(request, 'core/index.html', context)

def success(request):
    context = {}
    return render(request, 'core/success.html', context)


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            reg = form.save()
            z = Zip.objects.get(zip=reg.zip)
            if z.mail_only:
                return redirect(reverse('mail', kwargs={'zip': reg.zip}))

            # redirect to a new URL:
            return redirect(z.link)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'core/register.html', context)


def mail(request,zip):
    z = Zip.objects.get(zip=zip)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            mail = form.save()

            # process the data in form.cleaned_data as required




            # redirect to a new URL:
            return redirect('success')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = MailForm(initial={'zip':z.zip,'state':z.state})

    context = {'form': form,'zip':z}
    return render(request, 'core/mail.html', context)

