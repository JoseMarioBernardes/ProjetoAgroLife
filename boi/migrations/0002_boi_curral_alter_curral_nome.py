# Generated by Django 5.1.3 on 2024-12-03 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boi',
            name='curral',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='boi_curral', to='boi.curral'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curral',
            name='nome',
            field=models.CharField(max_length=45),
        ),
    ]
