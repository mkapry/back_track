# Generated by Django 2.0.3 on 2018-03-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hole',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
