# Generated by Django 5.1.1 on 2024-10-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_isapproved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='isApproved',
            field=models.IntegerField(choices=[(-1, 'Pending'), (0, 'Declined'), (1, 'Approved')], default=-1),
        ),
    ]
