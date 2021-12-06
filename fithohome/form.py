from django.forms import ModelForm
from .models import userdata,renting_form_data
from django import forms

class userform(ModelForm):
    class Meta:
        model=userdata
        fields= ['name','phone','email','height','weight','fat','build']
        FAT_CHOICES = (
            ('belly','BELLY'),
            ('thigh', 'THIGH'),
            ('legs','LEGS'),
            ('back','BACK'),
            ('arms','ARMS'),
        )
        widgets= {
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'phone':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control'
            }),
             'height':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'In cms'
            }),

             'weight':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'In kgs'
            }),
             'fat':forms.Select(choices=FAT_CHOICES,attrs={
                'class':'form-control',
            }),
             'build':forms.Select(choices=FAT_CHOICES,attrs={
                'class':'form-control'
            }),
        }


class renting_form(ModelForm):
    class Meta:
        model=renting_form_data
        fields= ['name','phone','add']
        widgets= {
            'name':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'phone':forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'add':forms.TextInput(attrs={
                'class':'form-control'
            }),
        }
        
