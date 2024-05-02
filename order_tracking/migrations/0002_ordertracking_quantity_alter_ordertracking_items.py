# Generated by Django 4.2.7 on 2024-05-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertracking',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ordertracking',
            name='items',
            field=models.JSONField(default={'product_name': ''}),
        ),
    ]
