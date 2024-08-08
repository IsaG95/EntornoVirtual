from django.contrib import admin
from .models import Student, Measurement, FoodLog, Recommendation, AnalysisResult

# Register your models here.

admin.site.register(Student)
admin.site.register(Measurement)
admin.site.register(FoodLog)
admin.site.register(Recommendation)
admin.site.register(AnalysisResult)

