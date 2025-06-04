from django.urls import reverse

def sidebar_links(request):
    return {
        'sidebar_items': [
            {'name': 'Home', 'url': reverse('homepage')},
        ]
    }