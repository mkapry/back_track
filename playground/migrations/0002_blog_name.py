# Generated by Django 2.0.3 on 2018-04-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
