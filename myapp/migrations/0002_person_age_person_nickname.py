# Generated by Django 4.2.1 on 2023-05-26 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='nickName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
