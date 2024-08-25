from django.db import models
from cliente.models import cliente

# Create your models here.
class compras(models.Model):
    cliente = models.ForeignKey(
        to= cliente,
        blank=False,
        null=False,
        max_length=50,
        on_delete=models.CASCADE
    )

    valor = models.FloatField(
        null=False,
        blank=False
    )

    data = models.DateField(
        null=False,
        blank=False
    )