# Generated by Django 2.2.2 on 2019-10-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20191024_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='commercial_name',
            field=models.CharField(max_length=30),
        ),
    ]
