# Generated by Django 4.0.5 on 2022-06-20 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Content',
            new_name='Text',
        ),
    ]
