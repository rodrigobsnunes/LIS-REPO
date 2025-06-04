from .conexoes import obter_ordens_servico
from ordens_servico.models import OrdemServicoModel,Status
from datetime import datetime
from django.utils.timezone import make_aware

def atualizar_bd_ordens_servico():
    novas_os = obter_ordens_servico()
    for dados in novas_os:
        ordem = OrdemServicoModel(nr_os_externo=dados['nr_os']
                                ,solicitante=dados['solicitante']
                                ,descricao = dados['descricao']
                                ,servico = dados['servico'])
        ordem.save()

def assume_os(lista_ids,responsavel):
    queryset = OrdemServicoModel.objects.filter(pk__in=lista_ids,status=Status.ABERTA)
    queryset.update(responsavel=responsavel,ts_inicio=make_aware(datetime.now()),status=Status.INICIADA)

def encerra_os(lista_ids):
    queryset = OrdemServicoModel.objects.filter(pk__in=lista_ids,status=Status.INICIADA)
    queryset.update(ts_conclusao=make_aware(datetime.now()),status=Status.CONCLUIDA)
