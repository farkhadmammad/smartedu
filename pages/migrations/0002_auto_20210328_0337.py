# Generated by Django 3.1.7 on 2021-03-27 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='Ad',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='Soyad',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='Telefon',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='mesaj',
        ),
    ]
