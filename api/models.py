from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    student_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    grado = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'  # Nombre de la tabla existente

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Measurement(models.Model):
    measurement_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fecha = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'measurements'  # Nombre de la tabla existente

class FoodLog(models.Model):
    MEAL_TYPE_CHOICES = [
        ('Desayuno', 'Desayuno'),
        ('Almuerzo', 'Almuerzo'),
        ('Cena', 'Cena'),
        ('Merienda', 'Merienda'),
    ]

    log_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_comida = models.CharField(max_length=50, choices=MEAL_TYPE_CHOICES)
    desc_alimentos = models.TextField()
    calorias = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'food_logs'  # Nombre de la tabla existente

class Recommendation(models.Model):
    recommendation_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fecha = models.DateField()
    recomendacion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recommendations'  # Nombre de la tabla existente

class AnalysisResult(models.Model):
    result_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fecha_analisis = models.DateField()
    bmi_prediccion = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    riesgo_salud = models.CharField(max_length=100, null=True, blank=True)
    recomendacion_dieta = models.TextField(null=True, blank=True)
    otros_estatus = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'analysis_results'  # Nombre de la tabla existente
