from django.contrib import admin

from api.models import Student, Discipline, ReportCard, Grades

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date']

class DisciplineAdmin(admin.ModelAdmin):
    list_display = ['name', 'workload']

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'due_date']

class GradesAdmin(admin.ModelAdmin):
    list_display = ['report_card', 'discipline', 'grade']

admin.site.register(Student, StudentAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(ReportCard, ReportCardAdmin)
admin.site.register(Grades, GradesAdmin)