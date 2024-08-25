from django.contrib import admin
from compras.models import compras

# Register your models here.
class comprasadmin(admin.ModelAdmin):
    # Não foi possivel inserir a coluna de gerentes por ser do tipo ManyToManyField
    list_display = ("cliente", "valor", "data", )
    list_display_links = ("cliente", "valor", "data", )
    search_fields = ("cliente", "valor", "data", )
    list_filter = ("cliente", "valor", "data", )

    list_per_page = 20


admin.site.register(compras, comprasadmin)