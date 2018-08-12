from django.urls import path

from . import views

app_name = 'ideas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:id>/edit/', views.editView, name='edit'),
    path('add/', views.addView, name='add'),    
]
