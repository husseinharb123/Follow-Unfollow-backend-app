# Generated by Django 4.0.3 on 2022-06-18 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_pc_barcode_computernadscreen_barcode_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='printer',
            old_name='ipaddress',
            new_name='address',
        ),
    ]
