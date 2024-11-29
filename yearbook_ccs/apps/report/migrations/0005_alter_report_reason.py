# Generated by Django 5.1.1 on 2024-11-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_report_report_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reason',
            field=models.IntegerField(choices=[(0, 'Nudity or sexual activity'), (1, 'Bullying or harassment'), (2, 'Suicide, self-injury, or eating disorder'), (3, 'Violence, hate, or exploitation'), (4, 'Selling or promoting restricted items'), (5, 'Scam, fraud, or impersonation')], default=1),
        ),
    ]