
import random

def obter_ordens_servico(qtd_os=3):
    #Lógica para chamar a API externa que fornece as OSs disponíveis para o LIS.
    #Implementado um mockup no momento
    lista_os = []
    for i in range(0,qtd_os):
        rand = random.randint(0,10000)
        ordem = {'nr_os'      : rand
                ,'solicitante': f'Cliente {rand}'
                ,'servico'    : random.randint(0,3)
                ,'descricao'  : f'OS de mockup número {rand}'}
        lista_os.append(ordem)

    return lista_os
