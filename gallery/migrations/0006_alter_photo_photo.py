# Generated by Django 4.1.5 on 2023-01-21 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_photo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]