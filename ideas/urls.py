from django.urls import path, include, re_path
from django.urls import reverse
from . import views
from .models import Idea
from rest_framework import routers


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api', views.IdeaViewSet)

app_name = 'ideas'

urlpatterns = [
    #path('api', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('details/<int:pk>/', views.DetailMiniView.as_view(), name='detailmini'),
    path('<int:id>/edit/', views.editView, name='edit'),
    # path('<int:id>/proposal/', include('tinymce.urls'), name='editor'),
    path('tinymce/', include('tinymce.urls')),
    path('add/', views.addView, name='add'),
    path('addgroup', views.AddGroup.as_view(success_url='/ideas/'),
         name='addgroup'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('results/', views.SearchResultsView.as_view(), name='search_results'),
    path('<str:slug>/', views.GroupView.as_view(), name='groupview'),
    
    path('contact', views.ContactView.as_view(), name='contact'),
    path('', include('social_django.urls', namespace='social')),
    
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
