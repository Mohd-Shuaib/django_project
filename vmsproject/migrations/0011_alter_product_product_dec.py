# Generated by Django 4.0.3 on 2022-04-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsproject', '0010_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_dec',
            field=models.CharField(max_length=500),
        ),
    ]
