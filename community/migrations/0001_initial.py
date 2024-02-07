# Generated by Django 5.0 on 2024-02-05 22:13

import community.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('category', models.CharField(choices=[('몇대몇', '몇대몇'), ('영상 공유', '영상 공유'), ('자유', '자유'), ('질문', '질문')], max_length=20, verbose_name='카테고리')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=community.models.post_image_path)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='community.post')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='community.post')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='community.post')),
            ],
            options={
                'unique_together': {('user', 'post')},
            },
        ),
    ]