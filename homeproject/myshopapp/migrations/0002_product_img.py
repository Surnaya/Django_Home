# Generated by Django 4.2.11 on 2024-05-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myshopapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="product_images/"),
        ),
    ]
