# Generated by Django 3.2.8 on 2021-12-02 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_api'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='api',
            options={'verbose_name_plural': 'API'},
        ),
    ]