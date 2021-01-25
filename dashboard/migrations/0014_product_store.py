# Generated by Django 3.1 on 2021-01-20 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210120_0111'),
        ('dashboard', '0013_remove_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.store'),
            preserve_default=False,
        ),
    ]