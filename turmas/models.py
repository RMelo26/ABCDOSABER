from django.db import models
from django.urls import reverse
from turmas.models import Turma


# Modelo representando um Tipo de Atividade
class Turmas(models.Model):
    """Modelo representando Instrutores"""
    numero = models.AutoField(primary_key=True)
    horario_aula = models.TimeField(help_text="Informe a turma do Aluno")
    data_inicial = models.DateField(help_text="Informe a hora em que a hora da aula da Turma")
    data_final = models.DateField(null=True, blank=True, help_text="Informe a data inicial da Turma")
    codigo_atividade = models.CharField(max_length=9, help_text="Informe o telefone do Instrutor")
    codigo_titulo = models.ForeignKey(null=True, blank=True, on_delete=models.SET_NULL, db_column="titulo_codigo")
    
    def __str__(self):
        return f'{self.codigo} - {self.descricao}'