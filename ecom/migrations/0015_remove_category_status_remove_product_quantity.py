# Generated by Django 4.0.5 on 2022-06-19 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0014_remove_product_slug_remove_product_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]