# Generated by Django 5.1.2 on 2024-11-09 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0002_cuisinecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cuisine.cuisine')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.DeleteModel(
            name='CuisineComment',
        ),
    ]
