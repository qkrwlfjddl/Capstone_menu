# Generated by Django 4.1 on 2023-10-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_orderstatus_status_changed_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
