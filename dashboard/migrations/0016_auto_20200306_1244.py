# Generated by Django 2.2.2 on 2020-03-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20200306_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referrallink',
            old_name='qrcode',
            new_name='qrcode_image',
        ),
        migrations.AlterField(
            model_name='referral',
            name='referral_token',
            field=models.TextField(default='q7W1vIjEX4X2lZ2Wrfgb', editable=False, max_length=1000),
        ),
    ]
