from django.db import models
from django.utils import timezone

from tipodeatividade.models import TipoDeAtividade
from instrutor.models import Instrutor
from alunos.models import Alunos

# Create your models here.
class Turmas (models.Model):
    """Modelo representando as Turmas"""
    numero = models.AutoField(primary_key=True,
                                 help_text='Número da Turma')
    horarioAula = models.TimeField(null=False,
                                    help_text='Informe o horário da Aula')
    duracaoAula = models.DurationField(null=False,
                                    help_text='Informe o horário da Aula')
    dataInicial = models.DateField(null=False, default=timezone.now(),
                                    help_text='Informe a Data inicial')
    
    dataFinal = models.DateField(null=True, blank=True,
                                    help_text='Informe a Data inicial')
    
    codigoTipoAtividade = models.ForeignKey(TipoDeAtividade,
                                         null=True,
                                         blank=True,
                                         on_delete=models.SET_NULL,
                                         help_text='codigo do tipo de atividade da Turma')
    
    matriculaMonitor = models.ForeignKey(Alunos,
                                         null=True,
                                         blank=True,
                                         on_delete=models.SET_NULL,
                                         help_text='Matrícula do Monitor da Turma')
    
    idInstrutor = models.ForeignKey(Instrutor,
                                    null=True, 
                                    on_delete=models.SET_NULL, 
                                    help_text='Identidade do Instrutor da Turma')
    
    
    def __str__(self):
        return f"turma: {self.numero} - dtinicial {self.dataInicial}"
    
    

class TurmaAluno(models.Model):
    numero_turma = models.ForeignKey(Turmas, on_delete=models.CASCADE,
                                     help_text="Número da turma do aluno.")
    matricula_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE,
                                        help_text="Matrícula do aluno da turma.")
    data_inicio_matricula = models.DateField(null=False,
                                             default=timezone.now,
                                             help_text="Data da matrícula do alino na turma")
    data_fim_matricula = models.DateField(null=True,
                                          help_text="Data de fim de matrícula do aluno na turma")

        
    def _str_(self):
        resposta = f'Turma: {self.numero_turma} - Aluno: {self.matricula_aluno}'
        return resposta
    
class Ausencia(models.Model):
    numero_turma = models.ForeignKey(Turmas, on_delete=models.CASCADE,
                                     help_text="Número da turma do aluno.")
    matricula_aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE,
                                        help_text="Matrícula do aluno da turma.")
    data_ausencia = models.DateField(null=False,
                                             default=timezone.now(),
                                             help_text="Data da falta do aluno na turma")
        
    def _str_(self):
        resposta = f'{self.numero_turma} - {self.matricula_aluno} - {self.data_ausencia("%d/%m/%y")}'
        data_fim_matricula = self.data_fim_matricula.strftime("%d/%m/%y") if self.data_fim_matricula else ''   
    
