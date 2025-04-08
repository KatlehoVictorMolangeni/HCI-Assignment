from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.Login, name='login'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('assignment', views.Manage_Assignment, name='manage'),
    path('quotes', views.view_quotes, name='quotes'),
    path('study-plan', views.study_plane, name='study'),
]