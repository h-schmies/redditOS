# Generated by Django 4.0.4 on 2022-05-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_user_salt'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
