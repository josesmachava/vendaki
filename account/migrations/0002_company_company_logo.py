# Generated by Django 2.2.2 on 2019-10-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(default='company_logo/default.jpg', upload_to='company_logo/'),
        ),
    ]