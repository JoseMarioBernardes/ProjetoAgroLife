# Generated by Django 5.1.3 on 2024-12-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0005_doenca_protocolo_protocolomedicamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boi',
            name='brinco',
            field=models.IntegerField(),
        ),
    ]
