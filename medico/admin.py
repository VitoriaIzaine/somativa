from django.contrib import admin
from .models import cadastro_medicos

class detMedico(admin.ModelAdmin):
    list_display = ('id','nome','especialidade','mostrar','foto')
    list_editable = ('mostrar',)
    list_display_links = ('nome',)
    search_fields = ('nome',)


admin.site.register(cadastro_medicos, detMedico)
