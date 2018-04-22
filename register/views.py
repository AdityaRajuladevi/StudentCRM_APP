from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.forms.forms import NON_FIELD_ERRORS
from django.conf import settings
from django.urls import reverse
from django.contrib import messages

from decimal import *

from .forms import RegisterForm
from .models import NewUser


# Create your views here.
def register_new(request, template='register/register.html'):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Create the User record
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password)

            # Create Subscriber Record
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            newUser = NewUser(address_one=address_one, address_two=address_two,
                             city=city, state=state, user_rec=user)

            user.save()
            a_u = authenticate(username=username, password=password)
            if a_u is not None:
                if a_u.is_active:
                    login(request, a_u)
                    # newUser.save()
                    return HttpResponseRedirect(reverse('student_list'))
                else:
                    return HttpResponseRedirect(
                        reverse('django.contrib.auth.views.login')
                    )
            else:
                return HttpResponseRedirect(reverse('register_new'))


    else:
        form = RegisterForm()
        form.error_messages.clear()
    return render(request, template,{'form':form})
