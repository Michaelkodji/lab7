# Generated by Django 4.1.2 on 2023-07-10 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('article_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('article_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('category_libelle', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('profil_id', models.IntegerField(primary_key=True, serialize=False)),
                ('profil_libelle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='voteArtcile',
            fields=[
                ('vote_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('vote_decision', models.BooleanField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.article', verbose_name='article_voted')),
                ('editeur_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.usermanager', verbose_name='user_who_voted')),
            ],
        ),
        migrations.CreateModel(
            name='observation',
            fields=[
                ('observation', models.BigIntegerField(primary_key=True, serialize=False)),
                ('observation_text', models.TextField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.article', verbose_name='editor_opinion')),
                ('editeur_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.usermanager', verbose_name='user_who_give_opinion')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.article', verbose_name='article_comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.usermanager', verbose_name='user_who_comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.category', verbose_name='article_category'),
        ),
        migrations.AddField(
            model_name='article',
            name='editeur_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backlab.usermanager', verbose_name='user_who_edit'),
        ),
    ]
