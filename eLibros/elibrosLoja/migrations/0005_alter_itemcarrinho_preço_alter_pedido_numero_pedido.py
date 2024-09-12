# Generated by Django 5.0.3 on 2024-09-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrosLoja', '0004_remove_itemcarrinho_slug_alter_pedido_numero_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='preço',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default='779832021568', max_length=12, primary_key=True, serialize=False),
        ),
    ]
