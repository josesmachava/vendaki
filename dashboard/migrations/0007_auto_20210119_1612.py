# Generated by Django 2.2.2 on 2021-01-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_orderproduct_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, max_length=30),
        ),
    ]
