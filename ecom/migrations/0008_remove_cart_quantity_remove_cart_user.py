# Generated by Django 4.0.5 on 2022-06-10 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
