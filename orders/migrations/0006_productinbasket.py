# Generated by Django 5.1.1 on 2024-11-22 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_price_pre_item_productinorder_price_per_item'),
        ('products', '0006_rename_type_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]
