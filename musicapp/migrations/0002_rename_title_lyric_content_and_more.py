# Generated by Django 4.1.2 on 2022-10-27 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lyric", old_name="title", new_name="content",
        ),
        migrations.RemoveField(model_name="lyric", name="date_released",),
    ]
