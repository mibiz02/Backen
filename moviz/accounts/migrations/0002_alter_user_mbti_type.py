# Generated by Django 3.2.13 on 2022-11-21 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='MBTI_type',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
