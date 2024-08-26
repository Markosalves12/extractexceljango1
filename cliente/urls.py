from cliente.views import view_data, exportar_excel
from django.urls import path


urlpatterns = [
    path('', view_data, name='view_data'),
    path('exportar_excel', exportar_excel, name='exportar_excel'),
]