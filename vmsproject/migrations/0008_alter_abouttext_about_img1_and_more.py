# Generated by Django 4.0.3 on 2022-04-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsproject', '0007_remove_abouttext_about_img5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouttext',
            name='about_img1',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='abouttext',
            name='about_img2',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='abouttext',
            name='about_img3',
            field=models.ImageField(default='', upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='abouttext',
            name='about_img4',
            field=models.ImageField(default='', upload_to='pics'),
        ),
    ]
