# Generated by Django 4.0.3 on 2022-03-07 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_playback_options_song_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.song')),
            ],
        ),
    ]
