# Generated by Django 4.0.2 on 2022-02-06 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='name_eng',
            new_name='name_en',
        ),
    ]