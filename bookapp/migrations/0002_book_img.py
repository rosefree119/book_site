# Generated by Django 4.2.9 on 2024-01-18 13:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='roll'),
            preserve_default=False,
        ),
    ]
