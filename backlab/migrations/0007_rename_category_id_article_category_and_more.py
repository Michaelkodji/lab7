# Generated by Django 4.1.2 on 2023-07-11 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlab', '0006_alter_comment_comment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='editeur_id',
            new_name='editeur',
        ),
    ]
