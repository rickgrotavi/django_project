# Generated by Django 3.1 on 2020-08-10 09:27

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(default='Description')),
                ('keywords', models.CharField(default='Key words', max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('visible', models.BooleanField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id', '-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Кагория')),
                ('slug', models.SlugField(null=True, verbose_name='Транслит')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), size=None)),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата комментария')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cooker_app.article')),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='cooker_app.category'),
        ),
    ]