# Generated by Django 2.2.2 on 2021-01-19 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
