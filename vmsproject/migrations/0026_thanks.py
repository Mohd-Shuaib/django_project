# Generated by Django 4.0.3 on 2022-05-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsproject', '0025_rename_navtitle_navigationbar_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='thanks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('dec', models.TextField()),
                ('Button_Url', models.URLField()),
                ('Button_Text', models.CharField(max_length=255)),
            ],
        ),
    ]
