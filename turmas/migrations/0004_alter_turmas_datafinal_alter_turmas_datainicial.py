# Generated by Django 4.2.18 on 2025-02-14 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0003_alter_turmas_datafinal_alter_turmas_datainicial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turmas',
            name='dataFinal',
            field=models.DateField(blank=True, help_text='Informe a Data inicial', null=True),
        ),
        migrations.AlterField(
            model_name='turmas',
            name='dataInicial',
            field=models.DateField(default=datetime.datetime(2025, 2, 14, 23, 34, 34, 549405, tzinfo=datetime.timezone.utc), help_text='Informe a Data inicial'),
        ),
    ]
