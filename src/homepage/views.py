from django.shortcuts import render
from django.urls import reverse

def home(request):
    app_links = [] # Será preenchida conforme as demais funcionalidades forem implementadas
    return render(request, 'home.html', {'app_links': app_links})