# Generated by Django 4.1.2 on 2023-08-14 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_productimages"),
    ]

    operations = [
        migrations.DeleteModel(name="ColorVariant",),
        migrations.RemoveField(model_name="product", name="category",),
        migrations.RemoveField(model_name="productimages", name="product",),
        migrations.DeleteModel(name="QuantityVariant",),
        migrations.DeleteModel(name="SizeVariant",),
        migrations.DeleteModel(name="Category",),
        migrations.DeleteModel(name="Product",),
        migrations.DeleteModel(name="ProductImages",),
    ]
