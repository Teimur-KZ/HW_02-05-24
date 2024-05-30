# Generated by Django 5.0.6 on 2024-05-30 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication_app', '0002_alter_profile_email_customer'),
        ('products_app', '0004_productsize_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Способ доставки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('min_total_price_for_free_delivery', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Способ оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_order', models.CharField(max_length=255, verbose_name='Номер заказа')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена доставки')),
                ('delivery_status', models.CharField(max_length=255, verbose_name='Статус доставки')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Общая цена')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders_app.deliveryoptions', verbose_name='Способ доставки')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication_app.profile', verbose_name='Профиль пользователя')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders_app.paymentoptions', verbose_name='Способ оплаты')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_items', to='orders_app.order')),
                ('product_size_quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_order_items', to='products_app.productsizequantity')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_items', to='orders_app.order')),
                ('product_size_quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_order_items', to='products_app.productsizequantity')),
            ],
        ),
    ]
