# Generated by Django 2.2.2 on 2020-03-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20200306_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='order_product',
        ),
        migrations.AlterField(
            model_name='referral',
            name='referral_token',
            field=models.TextField(default='isJWbwNMfh5tnujl4wHD', editable=False, max_length=1000),
        ),
    ]
