from django.contrib.auth.models import AbstractUser
from django.db import models

from validators import *

class Cliente(AbstractUser):
    
    '''
    - username --> obrigatório por padrão
    - password --> obrigatório


    CAMPOS OPCIONAIS:

    - first_name
    - last_name
    ...
    - last_login
    - date_joined

    '''

    nome = models.CharField(null=True, validators=[nao_nulo])
    CPF = models.CharField(null=True, max_length=15)

    genero_choices = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("NB", "Não-binário"),
        ("OU", "Outro")
    )

    genero = models.CharField(max_length=20, choices=genero_choices, default="F", null=True)
    outro_genero = models.CharField(max_length=50, blank=True, null=True)
    dt_nasc = models.DateField()



    #sobreescrita do método save para essa classe
    def save(self, *args, **kwargs):
        if self.genero != 'other':
            self.outro_genero = ''
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username