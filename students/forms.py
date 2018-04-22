from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'desc', 'address_one',
                  'address_two', 'city', 'state', 'phone',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Name',
                    'class':'col-md-12 form-control'
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder':'Enter a description',
                    'class':'form-control'
                }
            ),
            'address_one': forms.TextInput(
                attrs={
                    'placeholder':'Street Address',
                    'class':'gi-form-addr form-control'
                }
            ),
            'address_two': forms.TextInput(
                attrs={
                    'placeholder':'Suite, PO, etc',
                    'class':'gi-form-addr form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder':'City',
                    'class':'gi-form-addr form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder':'State',
                    'class':'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Phone',
                    'class':'gi-form-addr form-control'
                }
            ),
        }
