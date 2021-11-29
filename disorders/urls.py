from django.urls import path
from disorders import views

urlpatterns = [
    path('disorder/', views.disorder, name='disorder'),
]
