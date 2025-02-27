from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividade

app_name = 'tipodeatividade'

# Create your views here.
def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    contexto = {
        'tipodeatividade' : lista_tipodeatividade, 
    }
    
    
def carregar_cadastro(request):
    return render (request, 'tipodeatividade/cadastrar_tipodeatividade.html')

def cadastrar (request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        topodeatividade = TipoDeAtividade(
            descricao = dados_tipodadetividade['descricao']
        )
        tipodeatividade.save()
            
    return render(request, 'tipodeatividade/tipodeatividade.html', context = contexto)