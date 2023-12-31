# Generated by Django 4.1.3 on 2023-12-08 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0002_alter_artist_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='tunaapi.genre')),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='tunaapi.song')),
            ],
        ),
    ]
