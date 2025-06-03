from django.shortcuts import render
from django.forms import ModelForm
from .models import OrdemServicoModel
from django.views import View
from .core.ordens_servico import atualizar_bd_ordens_servico
from django.http import JsonResponse

class CriacaoOrdemServicoForm(ModelForm):
    class Meta:
        model = OrdemServicoModel
        fields = ['nr_os_externo','solicitante','servico','descricao']

class AssuncaoOrdemServicoForm(ModelForm):
    class Meta:
        model = OrdemServicoModel
        fields = ['responsavel']

class AtualizarBDOSView(View):
    def get(self,request):
        atualizar_bd_ordens_servico()
        return JsonResponse({'message': 'Atualização do banco de dados de OS concluída com sucesso.'})

class OSHomeView(View):
    def get(self,request):
        ordens_servico = OrdemServicoModel.objects.all()
        return render(request,'os_home.html',{'ordens_servico': ordens_servico})
