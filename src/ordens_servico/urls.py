from django.urls import path
from . import views

app_name = 'ordens_servico'

urlpatterns = [
    path('', views.OSHomeView.as_view(), name='os_home'),
    path('api/atualizar', views.AtualizarBDOSView.as_view(), name='atualizar_os'),
]