from django.shortcuts import render, redirect

# Create your views here.
from core.forms import RegisterForm, MailForm
from core.models import Zip

from django.urls import reverse

from django.shortcuts import get_object_or_404



def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            reg = form.save()


            reg.utm_source = request.GET.get('utm_source', '')
            reg.utm_medium = request.GET.get('utm_medium', '')
            reg.utm_campaign = request.GET.get('utm_campaign', '')

            reg.save()



            z = Zip.objects.get(zip=reg.zip)
            return redirect(reverse('next', kwargs={'zip': reg.zip}))


    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'core/index.html', context)




def next(request,zip):
    z = get_object_or_404(Zip, zip=zip)
    context = {'zip': z}
    if z.state == 'ND':
        return render(request, 'core/nd.html', context)

    return render(request, 'core/next.html', context)






def success(request):
    context = {}
    return render(request, 'core/success.html', context)



def mail(request,zip):
    # z = Zip.objects.get(zip=zip)
    z = get_object_or_404(Zip, zip=zip)
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

