# Generated by Django 4.0.5 on 2022-06-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0013_order_delete_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
    ]