from .conexoes import obter_ordens_servico
from ordens_servico.models import OrdemServicoModel

def atualizar_bd_ordens_servico():
    novas_os = obter_ordens_servico()
    for dados in novas_os:
        ordem = OrdemServicoModel(nr_os_externo=dados['nr_os']
                                ,solicitante=dados['solicitante']
                                ,descricao = dados['descricao']
                                ,servico = dados['servico'])
        ordem.save()