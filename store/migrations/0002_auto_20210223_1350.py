# Generated by Django 3.1.3 on 2021-02-23 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='shippigAddress',
            new_name='ShippingAddress',
        ),
    ]