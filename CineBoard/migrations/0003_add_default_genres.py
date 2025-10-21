from django.db import migrations


def create_default_genres(apps, schema_editor):
    Genre = apps.get_model('CineBoard', 'Genre')
    for name in ['Хоррор', 'Фэнтези']:
        Genre.objects.get_or_create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('CineBoard', '0002_alter_cineitem_channel_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.RunPython(create_default_genres, reverse_code=migrations.RunPython.noop),
    ]
