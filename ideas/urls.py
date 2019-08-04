from django.urls import path, include
from django.urls import reverse
from . import views

app_name = 'ideas'
urlpatterns = [
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
    path('<slug:slug>/', views.GroupView.as_view(), name='groupview'),
    
    path('contact', views.ContactView.as_view(), name='contact'),
    path('', include('social_django.urls', namespace='social')),
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'
