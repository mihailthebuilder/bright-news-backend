# Generated by Django 3.1.6 on 2021-02-09 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('score', models.SmallIntegerField()),
                ('random_positive_text', models.TextField()),
                ('random_negative_text', models.TextField()),
                ('raw_data', models.JSONField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
