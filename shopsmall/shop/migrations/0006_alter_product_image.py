# Generated by Django 4.2.10 on 2024-05-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/static/images/apple.jpg', null=True, upload_to='static/images/'),
        ),
    ]
