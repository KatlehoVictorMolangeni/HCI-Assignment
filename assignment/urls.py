from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('login/', views.Login, name='login'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('assignment', views.Manage_Assignment, name='manage'),
    path('quotes', views.view_quotes, name='quotes'),
    path('study-plan', views.study_plane, name='study'),
    path('register/', views.register, name='register'),
    path('added/',views.saved, name='added'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)