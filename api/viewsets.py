from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.pagination import PageNumberPagination

from api.models import Student, Discipline, ReportCard, Grades
from api.serializers import CardsSerializer, StudentSerializer, DisciplineSerializer,\
                            ReportCardSerializer, GradesSerializer
from api.utils import CustomAllowAnyPost
from rest_framework.decorators import permission_classes

# Create your views here.

@permission_classes([CustomAllowAnyPost])
class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DisciplineViewSet(ModelViewSet):

    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class ReportCardViewSet(ModelViewSet):

    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer

class GradesViewSet(ModelViewSet):

    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

class CardViewSet(ReadOnlyModelViewSet):

    queryset = Grades.objects.all()
    serializer_class = CardsSerializer

    #Override queryset to only return grade for logged user
    def get_queryset(self):
        return Grades.objects.filter(report_card__student__user=self.request.user)

