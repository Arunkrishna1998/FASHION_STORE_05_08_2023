# Generated by Django 4.2.3 on 2023-07-18 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_cart_items_product_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_items',
            name='product_variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sizevariant'),
        ),
    ]
