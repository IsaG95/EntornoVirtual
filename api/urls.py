from django.urls import path, include
from rest_framework import routers
from . import views

# Configuración del enrutador de REST framework
router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet) # Ruta para la vista StudentViewSet
router.register(r'measurements', views.MeasurementViewSet)
router.register(r'foodlogs', views.FoodLogViewSet)
router.register(r'recommendations', views.RecommendationViewSet)
router.register(r'analysisresults', views.AnalysisResultViewSet)

# URL patterns para incluir las rutas definidas en el enrutador
urlpatterns = [
    path('', include(router.urls)) # Incluye todas las rutas del enrutador
]
