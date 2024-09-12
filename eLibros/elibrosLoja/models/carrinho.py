from django.db import models
from elibrosLoja.models.itemcarrinho import ItemCarrinho

class Carrinho(models.Model):
    cliente = models.ForeignKey('accounts.Cliente', null=False, related_name="cliente_do_carrinho", on_delete=models.CASCADE)
    items = models.ManyToManyField(ItemCarrinho, null=True, related_name="items_do_carrinho", blank=True)

    def __str__(self):
        return f"Carrinho de {self.cliente.username} "
