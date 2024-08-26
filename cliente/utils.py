from compras.models import compras
from django.db.models import ExpressionWrapper, CharField, FloatField, DateField, F


def colect_dados(request):
    dados = compras.objects.annotate(
        nome_cliente = ExpressionWrapper(
            F('cliente__nome'),
            output_field=CharField()
        ),
        sobrenome_clinte = ExpressionWrapper(
            F('cliente__sobrenome'),
            output_field=CharField()
        ),
        valor_compra = ExpressionWrapper(
            F('valor'),
            output_field=FloatField()
        ),
        data_compra = ExpressionWrapper(
            F('data'),
            output_field=DateField()
        )
    )

    return dados