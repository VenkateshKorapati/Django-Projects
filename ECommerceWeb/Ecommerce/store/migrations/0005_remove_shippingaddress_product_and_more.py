# Generated by Django 4.0.1 on 2022-02-02 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_order_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='product',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
    ]
