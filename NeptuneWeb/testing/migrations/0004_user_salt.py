# Generated by Django 4.0.4 on 2022-05-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
