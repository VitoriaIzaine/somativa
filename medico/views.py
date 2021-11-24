from django.shortcuts import render


def index_medico(request):
    return render(request, 'medico/index.html')
