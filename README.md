-------------PROYECTO SEMINARIO UNIVERSIDAD MARIANO GALVEZ-------------------------

Sistema Web Para El Control Nutricional Y Seguimiento De Salud “Healthy Nutrition Meter, HNM” 

******Definición de la Arquitectura*****  

****Backend****

Framework: Se utiliza el framework Django

b. Creación de Servicios API REST
Se realizan las rutas y servicios necesarios para interactuar con la base de datos y realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
  /students: Para gestionar estudiantes (registro, actualización de información, etc.).
  /measurements: Para registrar y obtener medidas antropométricas.
  /food_logs: Para registrar y obtener registros alimenticios.
  /analysis: Para obtener resultados de análisis e inferencias.
  
c. Integración de la Base de Datos
Se utiliza una biblioteca ORM (Object-Relational Mapping) para facilitar la interacción con la base de datos. Con Django
En este caso utilizamos la base de datos *PostgreSql*.

d. Autenticación y Autorización
Se utiliza mecanismos de autenticación (por ejemplo, JWT) para asegurar que solo usuarios autorizados puedan acceder a ciertos servicios.


*****Desarrollo de la Inteligencia Artificial con TensorFlow****

a. Entrenamiento de Modelos
Datos de Entrenamiento: Para los datos de entrenamiento utilizamos los datos almacenados en las tablas measurements y food_logs.
Modelo: Se define y entrena los modelos de aprendizaje profundo utilizando TensorFlow.
b. Guardado del Modelo
Una vez entrenado, guarda el modelo para su uso en producción. 

c. Integración del Modelo en el Backend
Cargar el Modelo: En el backend, carga el modelo entrenado para realizar predicciones en tiempo real.
Inferencia: Se define endpoints que utilicen el modelo para realizar predicciones basadas en los datos proporcionados.

****Desarrollo del Frontend****

a. Interfaz de Usuario (UI)
Desarrollar la interfaz de usuario para que los usuarios puedan interactuar con el sistema. 

b. Visualización de Datos
Se implementa gráficas y tablas para mostrar los datos y resultados de los análisis. Bibliotecas como Chart.js o D3.js pueden ser útiles para esto.

****Pruebas y Despliegue****

a. Pruebas
Realiza pruebas unitarias y de integración para asegurar que todos los componentes funcionen correctamente.
Prueba la precisión del modelo de inteligencia artificial y ajusta los hiperparámetros si es necesario.

b. Despliegue
Implementa el backend y frontend en un servidor o plataforma en la nube, como AWS, Google Cloud, o Heroku.
Configura el servidor de base de datos y asegúrate de que todas las conexiones y servicios estén correctamente configurados.

7. Mantenimiento y Actualizaciones
Monitoreo: Implementa monitoreo para rastrear el rendimiento del sistema y del modelo de IA.
Actualizaciones: Mantén el sistema y el modelo actualizados con nuevos datos y mejoras.
