# Generated by Django 2.0.3 on 2019-02-13 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_order_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='type',
        ),
    ]
