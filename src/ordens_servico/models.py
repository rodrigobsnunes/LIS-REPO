from django.db import models

class Status(models.IntegerChoices):
    ABERTA = 0, 'Aberta'
    INICIADA = 1, 'Iniciada'
    CONCLUIDA = 2, 'Concluída'

class Servico(models.IntegerChoices):
    DESENVOLVIMENTO = 0, 'Desenvolvimento'
    MANUTENCAO = 1, 'Manutenção'
    CALIBRAÇÃO = 2, 'Calibração'
    TREINAMENTO = 3, 'Treinamento'

class OrdemServicoModel(models.Model):
    #um id automático já é gerado pelo Django
    nr_os_lis = models.IntegerField(primary_key=True)
    nr_os_externo = models.IntegerField(blank=True)
    solicitante = models.CharField(max_length=50)
    ts_solicitacao = models.DateTimeField(auto_now_add=True)
    servico = models.IntegerField(choices=Servico)
    descricao = models.CharField(max_length=300)
    status = models.IntegerField(choices=Status,default=Status.ABERTA)
    responsavel = models.CharField(max_length=50,null=True)
    ts_inicio = models.DateTimeField(null=True)
    ts_conclusao = models.DateTimeField(null=True)
    class Meta:
        db_table = 'ordens_servico'