# Generated by Django 2.2.2 on 2019-12-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20191219_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referral_token',
            field=models.CharField(default='j529FUnePHc2ywqaZ63Gyhfq0TukE4KU', editable=False, max_length=4),
        ),
    ]