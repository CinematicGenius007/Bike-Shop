from django.urls import path
from .views import bikes, bike, order, index

urlpatterns = [
    path('', index, name="index"),
    path('bikes/', bikes, name="bikes"),
    path('bikes/<int:pk>/', bike, name="bike"),
    path('order/<int:pk>/', order, name="order")
]
