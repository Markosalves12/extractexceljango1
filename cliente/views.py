from django.shortcuts import render
from compras.models import compras

# Create your views here.
def view_data(request):
    objects = compras.objects.all()

    return render(
        request,
        'relatorio.html',
        {
            'objects': objects
        }
    )