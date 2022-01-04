# Generated by Django 3.2.7 on 2021-10-18 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_biodata_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('judul', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Artikel',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AddField(
            model_name='artikel',
            name='kategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.kategori'),
        ),
    ]