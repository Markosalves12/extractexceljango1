from cliente.views import view_data
from django.urls import path


urlpatterns = [
    path('', view_data, name='view_data'),
]