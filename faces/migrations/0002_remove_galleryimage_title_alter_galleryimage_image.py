# Generated by Django 4.1.5 on 2023-02-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faces', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='title',
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]