# Generated by Django 4.1 on 2022-08-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_order_compelte_remove_order_transction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='compelte',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
