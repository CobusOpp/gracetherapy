from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contactView, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('list/', views.list, name='list'),

]
