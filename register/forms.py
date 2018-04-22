from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_one = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )

    address_two = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control','style': 'text-transform:uppercase;'}),max_length=2
    )

    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    #payment_error=forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control'}))
   # credit_card_no=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=16,min_length=16)


    class Meta:
        model = User
        fields = ('first_name','username', 'last_name', 'email', 'password1', 'password2' )


