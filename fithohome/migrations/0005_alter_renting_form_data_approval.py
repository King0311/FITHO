# Generated by Django 3.2.8 on 2021-12-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fithohome', '0004_alter_renting_form_data_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renting_form_data',
            name='approval',
            field=models.CharField(choices=[('approved', 'Approved'), ('declined', 'Declined.Sorry')], default='.....', max_length=100),
        ),
    ]