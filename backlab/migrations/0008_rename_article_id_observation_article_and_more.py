# Generated by Django 4.1.2 on 2023-07-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backlab', '0007_rename_category_id_article_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observation',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='observation',
            old_name='editeur_id',
            new_name='editeur',
        ),
        migrations.RenameField(
            model_name='voteartcile',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='voteartcile',
            old_name='editeur_id',
            new_name='editeur',
        ),
    ]
