# Generated by Django 3.2.8 on 2021-12-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fithohome', '0008_remove_renting_form_data_approval'),
    ]

    operations = [
        migrations.CreateModel(
            name='approval_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.BigIntegerField(default='', max_length=100)),
                ('add', models.CharField(default='', max_length=100)),
                ('approval', models.BooleanField(default=True)),
            ],
        ),
    ]
