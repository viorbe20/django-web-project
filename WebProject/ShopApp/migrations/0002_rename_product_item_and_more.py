# Generated by Django 5.0.2 on 2024-09-25 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='ItemCategory',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'ItemCategory', 'verbose_name_plural': 'itemCategories'},
        ),
    ]
