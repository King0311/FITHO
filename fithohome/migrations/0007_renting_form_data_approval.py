# Generated by Django 3.2.8 on 2021-12-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fithohome', '0006_renting_form_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='renting_form_data',
            name='approval',
            field=models.BooleanField(default=True),
        ),
    ]
