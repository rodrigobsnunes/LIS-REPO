from django.urls import reverse

def sidebar_links(request):
    return {
        'sidebar_items': [
            {'name': 'Home', 'url': reverse('homepage')},
            {'name': 'Ordens de Serviço', 'url': reverse('ordens_servico:os_home')},
        ]
    }