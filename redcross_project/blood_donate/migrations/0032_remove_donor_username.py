# Generated by Django 4.2.4 on 2023-08-25 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0031_donor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='username',
        ),
    ]
