from django.db import models

# Create your models here.

class blogs(models.Model):
    question1=models.CharField(max_length=100,default='')
    answer1=models.TextField(max_length=600,default='')
    img1=models.ImageField(upload_to="media")
    question2=models.CharField(max_length=100,default='')
    answer2=models.TextField(max_length=600,default='')
    img2=models.ImageField(upload_to="media")




class userdata(models.Model):
    FAT_CHOICES = (
        ('belly','BELLY'),
        ('thigh', 'THIGH'),
        ('legs','LEGS'),
        ('back','BACK'),
        ('arms','ARMS'),
    )
    name=models.CharField(max_length=100,default='')
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=100,default='')
    height=models.IntegerField()
    weight=models.IntegerField()
    fat=models.CharField(max_length=100, choices=FAT_CHOICES)
    build=models.CharField(max_length=100,choices=FAT_CHOICES)



class renting_form_data(models.Model):
    ORDER_CHOICES = (
        ('Approved','Approved'),
        ('Declined,Sorry', 'Declined'),
    )
    name=models.CharField(max_length=100,default='')
    phone=models.BigIntegerField(max_length=100,default='')
    add=models.CharField(max_length=100,default='')
    approval=models.CharField(max_length=100,choices=ORDER_CHOICES,default='.....')



    