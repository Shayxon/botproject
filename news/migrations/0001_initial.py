# Generated by Django 5.0.3 on 2024-03-18 09:20

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='news.email')),
            ],
        ),
    ]
