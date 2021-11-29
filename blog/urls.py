from django.urls import path
from . import views



urlpatterns = [
    path('blog/', views.all_blogs, name='blog'),
    path('category/<str:cats>/', views.CategoryView, name='category'),
    

]
