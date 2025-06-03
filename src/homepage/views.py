from django.shortcuts import render
from django.urls import reverse

def home(request):
    app_links = [{'name': 'Ordens de Serviço', 'url': reverse('ordens_servico:os_home')}]
    return render(request, 'home.html', {'app_links': app_links})