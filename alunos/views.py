from django.shortcuts import render
from django.http import HttpResponse
from alunos.models import Alunos
from alunos.forms import AlunosForm

# Create your views here.
def listar(request):
    lista_aluno = Alunos.objects.all()
    context = {
            'alunos' : lista_aluno,
    }
    
    return render(request, 'alunos/listarAluno.html', context=context)

def carregar_cadastro(request):
    return render(request, 'alunos/cadastrarAlunos.html')


def cadastrar(request):
    form = AlunosForm(request.POST)
    if form.is_valid():
        dados_alunos = form.cleaned_data
        alunos = alunos(descricao=dados_alunos["descricao"])
        Alunos.save()

    return render(request, 'alunos/cadastrarAlunos.html')