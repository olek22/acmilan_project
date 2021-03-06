# Generated by Django 3.2.5 on 2022-03-17 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('stadium', models.CharField(max_length=64)),
                ('stadium_capacity', models.PositiveIntegerField(blank=True, null=True)),
                ('colors', models.CharField(blank=True, max_length=64, null=True)),
                ('nickname', models.CharField(blank=True, max_length=64, null=True)),
                ('web_site', models.URLField(blank=True, null=True)),
                ('description', models.TextField(default='')),
                ('club_crest', models.ImageField(blank=True, upload_to='club_crest')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
