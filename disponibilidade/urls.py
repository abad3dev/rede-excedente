
from os import path
from django.urls import path
from django.views.generic import TemplateView
from disponibilidade import views

urlpatterns = [
   path('disponibilizar/<int:id_material>/', views.disponibilizar, name='disponibilizar'),

]