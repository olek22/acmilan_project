# Generated by Django 4.0.2 on 2022-02-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acmilanweb', '0005_alter_club_stadium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='web_site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
