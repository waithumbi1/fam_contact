# Generated by Django 4.2.9 on 2024-02-06 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_remove_member_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(null=True),
        ),
    ]