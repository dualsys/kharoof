# Generated by Django 3.0.2 on 2020-01-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapi', '0005_auto_20200109_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('ledger_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('ledger_title', models.TextField(max_length=255, null=True)),
                ('login_id', models.CharField(max_length=255, null=True)),
                ('login_password', models.CharField(max_length=255, null=True)),
                ('contact_number', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('fcm_token', models.TextField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'ledgers',
            },
        ),
        migrations.AlterField(
            model_name='products',
            name='item_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='item_image',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='item_title',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='months',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='origin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='weight',
            field=models.CharField(max_length=255, null=True),
        ),
    ]