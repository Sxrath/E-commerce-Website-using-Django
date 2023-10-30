# Generated by Django 4.2.5 on 2023-09-25 06:36

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_alter_cart_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=5, default=Decimal('0.00'), max_digits=10),
        ),
    ]
