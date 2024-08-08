from rest_framework import viewsets
from .models import Student, Measurement, FoodLog, Recommendation, AnalysisResult
from .serializer import StudentSerializer, MeasurementSerializer, FoodLogSerializer, RecommendationSerializer, AnalysisResultSerializer 

# Vista para el modelo Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all() # Consulta todos los objetos del modelo
    serializer_class = StudentSerializer # Usa el serializador correspondiente

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class FoodLogViewSet(viewsets.ModelViewSet):
    queryset = FoodLog.objects.all()
    serializer_class = FoodLogSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class AnalysisResultViewSet(viewsets.ModelViewSet):
    queryset = AnalysisResult.objects.all()
    serializer_class = AnalysisResultSerializer
