# Generated by Django 4.1.3 on 2023-12-08 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunaapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='age',
            field=models.IntegerField(),
        ),
    ]
