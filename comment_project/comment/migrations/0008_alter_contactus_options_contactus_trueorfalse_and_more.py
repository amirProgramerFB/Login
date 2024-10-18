# Generated by Django 5.1.1 on 2024-10-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0007_alter_contactus_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='TrueOrFalse',
            field=models.CharField(max_length=100, null=True, verbose_name='تاییدی'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Email',
            field=models.CharField(max_length=250, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Fullname',
            field=models.CharField(max_length=200, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Ip',
            field=models.CharField(max_length=100, null=True, verbose_name='آیپی'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=255, verbose_name='متن پیام'),
        ),
    ]