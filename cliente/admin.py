from django.contrib import admin
from cliente.models import cliente

# Register your models here.
class clienteadmin(admin.ModelAdmin):
    # Não foi possivel inserir a coluna de gerentes por ser do tipo ManyToManyField
    list_display = ("nome", "sobrenome", )
    list_display_links = ("nome", "sobrenome", )
    search_fields = ("nome", "sobrenome", )
    list_filter =("nome", "sobrenome", )

    list_per_page = 20


admin.site.register(cliente, clienteadmin)