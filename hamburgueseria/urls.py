from django.urls import include, path
from . import views


urlpatterns = [
    path('ingrediente', views.lista_ingredientes),
    path('ingrediente/<int:id>', views.detalle_ingrediente),
    path('hamburguesa', views.lista_hamburguesas),
    path('hamburguesa/<int:id>', views.detalle_hamburguesa),
    path('hamburguesa/<int:id>/ingrediente/<int:idi>', views.preparacion),
    path("", views.home)
]