# Generated by Django 5.1.1 on 2024-11-16 07:51

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
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=200, null=True)),
                ('report_type', models.IntegerField(choices=[(0, 'Post'), (1, 'Comment'), (2, 'Profile')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Finished')], default=0)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('user_reported', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reported', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
