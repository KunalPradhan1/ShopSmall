# Generated by Django 4.2.10 on 2024-03-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_customers_bussiness'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
