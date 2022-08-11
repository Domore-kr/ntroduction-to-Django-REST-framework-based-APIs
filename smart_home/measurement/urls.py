from django.contrib import admin
from django.urls import path

from measurement.views import SensorsView, SensorView, MeasurementsList

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsList.as_view()),
]
