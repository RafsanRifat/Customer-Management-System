# Generated by Django 3.2.6 on 2021-08-03 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='Product',
            new_name='product',
        ),
    ]