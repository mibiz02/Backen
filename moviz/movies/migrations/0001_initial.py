# Generated by Django 3.2.13 on 2022-11-21 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField()),
                ('title', models.TextField()),
                ('poster_path', models.TextField()),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('release_date', models.TextField()),
                ('genre_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
