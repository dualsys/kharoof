# Generated by Django 3.0.2 on 2020-01-09 17:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customerapi', '0004_auto_20200109_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AddField(
            model_name='products',
            name='item_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
