# Generated by Django 4.0.3 on 2022-05-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmsproject', '0023_topbar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigationbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navurl', models.URLField()),
                ('navtitle', models.CharField(max_length=255)),
            ],
        ),
    ]