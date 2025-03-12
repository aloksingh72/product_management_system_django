from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/', login, name = "login"),
    path('dashboard/', dashboard, name = "dashboard"),
    path('delete-cat/<int:pk>/',delete_cat,name="delete-cat"),
    path('edit-cat/<int:pk>/',edit_cat,name="edit-cat"),
    path('add-product/',add_product,name="add-product"),
    path('delete-prod/<int:pk>/',delete_prod,name="delete-prod"),
    path('edit-prod/<int:pk>/',edit_prod,name="edit-prod"),
]
