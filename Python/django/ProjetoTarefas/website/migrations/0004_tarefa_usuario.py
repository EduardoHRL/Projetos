# Generated by Django 5.1.2 on 2024-11-22 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_tarefa_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(db_column='usu_codigo', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tarefas', to='website.usuario'),
            preserve_default=False,
        ),
    ]
