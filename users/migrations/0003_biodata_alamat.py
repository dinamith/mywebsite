# Generated by Django 3.2.7 on 2021-10-29 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_biodata_alamat'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
    ]
