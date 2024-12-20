# Generated by Django 5.1.3 on 2024-12-09 01:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elibrosLoja", "0018_alter_endereco_identificacao_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="endereco",
            name="criado_por",
        ),
        migrations.RemoveField(
            model_name="historicalendereco",
            name="criado_por",
        ),
        migrations.AlterField(
            model_name="historicalendereco",
            name="history_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="historicalpedido",
            name="numero_pedido",
            field=models.CharField(
                db_index=True, default="525197229763", max_length=12
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="numero_pedido",
            field=models.CharField(
                default="525197229763", max_length=12, primary_key=True, serialize=False
            ),
        ),
    ]
