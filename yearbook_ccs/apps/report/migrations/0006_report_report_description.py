# Generated by Django 5.1.1 on 2024-11-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_alter_report_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
