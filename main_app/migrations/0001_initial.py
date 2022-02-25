# Generated by Django 4.0.2 on 2022-02-25 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
            ],
        ),
    ]
