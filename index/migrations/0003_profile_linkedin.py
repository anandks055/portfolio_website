# Generated by Django 3.2 on 2023-01-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
