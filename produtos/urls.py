from django.urls import path
from .views import prod_lista
from .views import prod_novo
from .views import prod_update
from .views import prod_delete

urlpatterns = [
    path('c/', prod_novo, name="prod_novo"),
    path('r/', prod_lista, name="prod_lista"),
    path('u/<int:id>', prod_update, name="prod_update"),
    path('d/<int:id>', prod_delete, name="prod_delete"),
]