from django.shortcuts import render
from django.http import HttpResponse
from tipodeatividade.models import TipoDeAtividade
from tipodeatividade.forms import TipoDeAtividadeForm

app_name = "tipodeatividade"


# Create your views here.
def listar(request):
    lista_tipodeatividade = TipoDeAtividade.objects.all()
    contexto = {
        "tipodeatividade": lista_tipodeatividade,
    }
    return render(request, "tipodeatividade/cadastrar_tipodeatividade.html", contexto)


def carregar_cadastro(request):
    return render(request, "tipodeatividade/cadastrar_tipodeatividade.html")


def cadastrar(request):
    form = TipoDeAtividadeForm(request.POST)
    if form.is_valid():
        dados_tipodeatividade = form.cleaned_data
        tipodeatividade = TipoDeAtividade(descricao=dados_tipodeatividade["descricao"])
        tipodeatividade.save()

    return render(request, "tipodeatividade/tipodeatividade.html")
