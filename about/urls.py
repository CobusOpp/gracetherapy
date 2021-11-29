from django.urls import path
from about import views

urlpatterns = [
    path('dotnortje/', views.dotnortje, name='dotnortje'),
    path('gracetherapy/', views.gracetherapy, name='gracetherapy'),
    path('remedial/', views.remedial, name='remedial'),
]
