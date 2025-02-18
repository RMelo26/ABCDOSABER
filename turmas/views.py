from django.shortcuts import render
from django.http import HttpResponse

from turmas.models import Turma

# Create your views here.

def home(request):
    return render(request, 'escola.html')

def listar(request):
    lista_turma = Turma.objects.all()
    return HttpResponse(lista_turma)