# Generated by Django 4.1.3 on 2023-12-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0004_alter_songgenre_genre_id_alter_songgenre_song_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='songgenre',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='songgenre',
            old_name='song_id',
            new_name='song',
        ),
    ]
