from django.urls import path, include
from .views import CalculatorView

urlpatterns = [
    path('api', CalculatorView.as_view())
]
