# Generated by Django 5.1.3 on 2024-12-04 00:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0004_laboratorio_localaplicacaomedicamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doenca',
            fields=[
                ('id_doenca', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id_protocolo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('doenca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='protocolo_doenca', to='boi.doenca')),
            ],
        ),
        migrations.CreateModel(
            name='ProtocoloMedicamento',
            fields=[
                ('id_protocolomedicamento', models.AutoField(primary_key=True, serialize=False)),
                ('dosagem', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='boi.medicamento')),
                ('protocolo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='protocolomedicamento_protocolo', to='boi.protocolo')),
            ],
        ),
        migrations.CreateModel(
            name='ProtocoloRealizado',
            fields=[
                ('id_protocolorealizado', models.AutoField(primary_key=True, serialize=False)),
                ('data_protocolo_realizado', models.DateField()),
                ('boi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='protocolo_boi', to='boi.boi')),
                ('protocolo_medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='protocolo_protocolomedicamento', to='boi.protocolomedicamento')),
            ],
        ),
    ]
