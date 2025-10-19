from django.db import migrations

def taggit_tags(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(taggit_tags, reverse_code=migrations.RunPython.noop)
    ]
