from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
]
