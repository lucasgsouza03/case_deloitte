from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import Student, Discipline, ReportCard, Grades

class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

class DisciplineSerializer(ModelSerializer):

    class Meta:
        model = Discipline
        fields = '__all__'

class ReportCardSerializer(ModelSerializer):

    class Meta:
        model = ReportCard
        fields = '__all__'

class GradesSerializer(ModelSerializer):
    discipline = serializers.SlugRelatedField(slug_field='name', queryset=Discipline.objects.all())

    class Meta:
        model = Grades
        fields = '__all__'

class CardsSerializer(ModelSerializer):
    discipline = DisciplineSerializer(read_only=True)
    report_card = ReportCardSerializer(read_only=True)

    class Meta:
        model = Grades
        fields = '__all__'