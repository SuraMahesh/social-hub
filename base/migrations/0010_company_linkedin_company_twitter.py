# Generated by Django 4.0.4 on 2022-05-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
