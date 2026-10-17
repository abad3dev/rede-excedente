from django.urls import path
from instituicao import views

urlpatterns = [
    # Aqui nós chamamos a sua função "cadastrar_instituicao" que está no views.py
    path('cadastrar/', views.cadastrar_instituicao, name='cadastrar_instituicao'),
    path('', views.iniciar, name='iniciar'),
]