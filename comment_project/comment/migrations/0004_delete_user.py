# Generated by Django 5.1.1 on 2024-09-30 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_remove_contactus_id_contactus_ip_contactus_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
