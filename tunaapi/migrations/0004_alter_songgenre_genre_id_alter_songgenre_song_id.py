# Generated by Django 4.1.3 on 2023-12-09 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0003_songgenre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songgenre',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunaapi.genre'),
        ),
        migrations.AlterField(
            model_name='songgenre',
            name='song_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunaapi.song'),
        ),
    ]
