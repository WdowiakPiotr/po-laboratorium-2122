# Generated by Django 4.0.4 on 2022-05-25 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0002_diler_historia_serwisu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Samochod',
            new_name='Car',
        ),
        migrations.RenameModel(
            old_name='Diler',
            new_name='Dealer',
        ),
        migrations.RenameModel(
            old_name='Historia_serwisu',
            new_name='Service_history',
        ),
    ]