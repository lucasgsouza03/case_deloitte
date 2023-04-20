from django.db import models
from user.models import User

# Create your models here.

class Student(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    full_name = models.CharField(max_length=255, verbose_name=('Nome Completo'), null=True, blank=True)
    birth_date = models.DateField(verbose_name='Data de Nascimento')

    def __str__(self) -> str:
        return f"{self.full_name} - {self.user.email}"
    
    class Meta:
        verbose_name = ("Aluno")
        verbose_name_plural = ("Alunos")

class Discipline(models.Model):

    name = models.CharField(max_length=255, verbose_name='Nome')
    workload = models.PositiveIntegerField(verbose_name='Carga Horária')

    def __str__(self) -> str:
        return f"{self.name} - {self.workload}"
    
    class Meta:
        verbose_name = ("Disciplina")
        verbose_name_plural = ("Disciplinas")

class ReportCard(models.Model):

    due_date = models.DateField(verbose_name='Data da Entrega')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Aluno')

    def __str__(self) -> str:
        return f"Boletim - {self.student.full_name}"
    
    class Meta:
        verbose_name = ("Boletim")
        verbose_name_plural = ("Boletins")

class Grades(models.Model):

    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Disciplina')
    report_card = models.ForeignKey(ReportCard, on_delete=models.CASCADE, verbose_name='Boletim')
    grade = models.CharField(max_length=10, verbose_name=('Nota'), blank=True, null=True)

    def __str__(self) -> str:
        return f"Nota - {self.discipline.name}: ({self.grade})"
    
    class Meta:
        verbose_name = ("Nota")
        verbose_name_plural = ("Notas")