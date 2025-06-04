from django.contrib import admin
from .models import OrdemServicoModel

class OSAdmin(admin.ModelAdmin):
    list_display = ('nr_os_lis', 'solicitante','servico','status','responsavel')
    search_fields = ('responsavel','solicitante')
    list_filter = ('status','servico')

admin.site.register(OrdemServicoModel,OSAdmin)
