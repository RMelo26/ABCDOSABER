from django.shortcuts import render
from django.http import HttpResponse

from alunos.models import Alunos

# Create your views here.
def listar(request):
    lista_aluno = Alunos.objects.all()
    context = {
            'alunos': lista_aluno,
    }
    
    return render(request, 'aluno/listarAluno.html', context=context)