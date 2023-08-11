from django.urls import path
from . import views

urlpatterns = [
    path('probandoTemplate/', views.probandoTemplate, name='probandoTemplate'),
    path('index/', views.index, name='index')
]