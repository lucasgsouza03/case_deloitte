from django.urls import include, path
from rest_framework import routers

from api.viewsets import CardViewSet, StudentViewSet, DisciplineViewSet,\
                        ReportCardViewSet, GradesViewSet

api_router = routers.DefaultRouter()

api_router.register(r'student', StudentViewSet, basename='student')
api_router.register(r'discipline', DisciplineViewSet, basename='discipline')
api_router.register(r'report_card', ReportCardViewSet, basename='report_card')
api_router.register(r'grades', GradesViewSet, basename='grades')
api_router.register(r'cards', CardViewSet, basename='cards')

urlpatterns = [
    path('', include(api_router.urls)),
]
