# Generated by Django 4.2.1 on 2023-05-26 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_animalspecies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('animalSpecies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.animalspecies')),
            ],
        ),
    ]