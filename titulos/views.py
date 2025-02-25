from django.shortcuts import render
from django.http import HttpResponse
from titulos.models import Titulos
from titulos.forms import TituloForm

# Create your views here.
def listar(request):
    lista_titulo = Titulos.objects.all()
    contexto = {
        'titulos' : lista_titulo 
    }
    
    return render(request, 'titulos/listar_titulos.html', context = contexto)

def carregar_cadastro(request):
    return render(request, 'titulos/cadastrarTitulos.html')
    
def cadastrar(request):
    form = TituloForm(request.POST)
    if form.is_valid():
        dados_titulo = form.cleaned_data
        titulo = Titulos(
            descricao= dados_titulo['descricao']
        )
        titulo.save()
        
    return render(request, 'titulos/cadastrarTitulos.html')