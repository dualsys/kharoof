# Generated by Django 3.0.2 on 2020-01-09 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='items',
        ),
        migrations.AlterModelTable(
            name='items',
            table=None,
        ),
    ]
