# Generated by Django 3.2.8 on 2021-12-06 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fithohome', '0007_renting_form_data_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='renting_form_data',
            name='approval',
        ),
    ]