from django.shortcuts import render,redirect
from django.forms import ModelForm
from .models import OrdemServicoModel
from django.views import View
from .core.ordens_servico import atualizar_bd_ordens_servico, encerra_os,assume_os
from django.http import HttpResponseRedirect,JsonResponse

class CriacaoOrdemServicoForm(ModelForm):
    class Meta:
        model = OrdemServicoModel
        fields = ['nr_os_externo','solicitante','servico','descricao']

class AssuncaoOrdemServicoForm(ModelForm):
    class Meta:
        model = OrdemServicoModel
        fields = ['responsavel']

class AtualizarBDOSView(View):
    def post(self,request):
        atualizar_bd_ordens_servico()
        return JsonResponse({'message': 'Atualização do banco de dados de OS concluída com sucesso.'})

class OSHomeView(View):
    def get(self,request):
        ordens_servico = OrdemServicoModel.objects.all()
        return render(request,'os_home.html',{'ordens_servico': ordens_servico})

    def post(self,request):
        action = request.POST.get('action')
        lista_os = request.POST.getlist('selected_items')
        responsavel = request.POST.get('responsavel')
        if action == 'assumir':
            assume_os(lista_os,responsavel)
        elif action == 'encerrar':
            encerra_os(lista_os)
        return HttpResponseRedirect(self.request.path)
    