# Generated by Django 4.0.2 on 2022-02-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_menu_phoro_restaurant_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='phoro',
            new_name='photo',
        ),
    ]
