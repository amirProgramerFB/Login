# Generated by Django 5.1.1 on 2024-10-01 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='Ip',
        ),
    ]
