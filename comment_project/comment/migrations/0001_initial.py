# Generated by Django 5.1.1 on 2024-09-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('family', models.CharField(max_length=250)),
                ('age', models.IntegerField(max_length=4)),
            ],
        ),
    ]
