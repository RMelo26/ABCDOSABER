from django.contrib import admin
from turmas.models import Turmas
from turmas.models import TurmaAluno
from turmas.models import Ausencia

# Register your models here.
admin.site.register(Turmas)
admin.site.register(TurmaAluno)
admin.site.register(Ausencia)