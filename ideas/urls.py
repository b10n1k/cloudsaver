from django.urls import path
from django.urls import reverse
from . import views

app_name = 'ideas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('details/<int:pk>/', views.DetailMiniView.as_view(), name='detailmini'),
    path('<int:id>/edit/', views.editView, name='edit'),
    path('add/', views.addView, name='add'),
    path('addgroup', views.AddGroup.as_view(success_url='/ideas/'), name='addgroup'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact', views.ContactView.as_view(), name='contact'),
]
