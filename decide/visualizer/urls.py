from django.urls import path
from .views import VisualizerView


urlpatterns = [
    path('', VisualizerView.as_view()),
]
