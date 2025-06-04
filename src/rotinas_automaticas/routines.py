from ordens_servico.routines import rotina_atualizar_bd_os
from .scheduler import scheduler

def configura_rotinas():
    scheduler.remove_all_jobs()
    
    scheduler.add_job(func=rotina_atualizar_bd_os
                    ,id='Rotina Buscar Novas OS'
                    ,replace_existing=True
                    ,trigger='interval'
                    ,minutes=30
                    )

    scheduler.start()
