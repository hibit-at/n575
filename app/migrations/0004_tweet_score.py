# Generated by Django 3.1 on 2021-06-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210618_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
