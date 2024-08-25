from django.db import models

# Create your models here.
class cliente(models.Model):
    nome = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )

    sobrenome = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'