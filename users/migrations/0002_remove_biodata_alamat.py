# Generated by Django 3.2.7 on 2021-10-29 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='alamat',
        ),
    ]