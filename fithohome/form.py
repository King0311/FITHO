from django.forms import ModelForm
from .models import userdata
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