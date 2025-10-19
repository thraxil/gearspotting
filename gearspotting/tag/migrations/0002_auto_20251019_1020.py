from django.db import migrations

def taggit_tags(apps, schema_editor):
    TaggitModel = apps.get_model("taggit", "Tag")
    MyModel = apps.get_model("tag", "Tag")
    for t in TaggitModel.objects.all():
        MyModel.objects.create(name=t.name, slug=t.slug)


class Migration(migrations.Migration):
    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(taggit_tags, reverse_code=migrations.RunPython.noop)
    ]
