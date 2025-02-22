from django.shortcuts import render
from django.http import HttpResponse
from titulos.models import Titulos

# Create your views here.
def listar(request):
    lista_titulo = Titulos.objects.all()
    contexto = {
        'titulos' : lista_titulo 
    }
    
    return render(request, 'tipodeatividade/listarTipoDeAtividade.html', context = contexto)