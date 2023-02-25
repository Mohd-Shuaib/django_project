# Generated by Django 4.0.3 on 2022-05-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsproject', '0030_exhibition_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner_Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial_Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
