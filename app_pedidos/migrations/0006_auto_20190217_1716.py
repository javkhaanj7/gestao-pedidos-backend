# Generated by Django 2.1.7 on 2019-02-17 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pedidos', '0005_auto_20190217_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='grand_total',
        ),
    ]
