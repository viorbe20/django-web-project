# Generated by Django 5.0.2 on 2024-09-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicesApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='ServicesApp'),
        ),
    ]