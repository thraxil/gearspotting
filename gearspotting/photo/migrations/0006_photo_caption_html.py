# Generated by Django 3.2.16 on 2023-02-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20170928_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='caption_html',
            field=models.TextField(blank=True, default=''),
        ),
    ]