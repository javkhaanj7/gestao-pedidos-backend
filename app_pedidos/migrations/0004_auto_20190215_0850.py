# Generated by Django 2.1.7 on 2019-02-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pedidos', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]