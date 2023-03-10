# Generated by Django 4.0.3 on 2022-04-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsproject', '0009_alter_abouttext_about_img1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_dec', models.CharField(max_length=300)),
                ('product_date', models.DateField()),
                ('product_image', models.ImageField(default='', upload_to='vmsproject/images')),
            ],
        ),
    ]
