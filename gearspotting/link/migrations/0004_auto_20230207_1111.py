# Generated by Django 3.2.16 on 2023-02-07 11:11
import markdown
from django.db import migrations


def forwards(apps, schema_editor):
    M = apps.get_model('link', 'Link')
    for m in M.objects.all():
        m.description_html = markdown.markdown(m.description)
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0003_link_description_html'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]