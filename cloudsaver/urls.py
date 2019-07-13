from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from ideas import views

urlpatterns = [
    path('ideas/', include('ideas.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    #path('logout/', views.logout, name='logout'),
    path('', include('social_django.urls', namespace='social')),
    #path('tinymce/', include('tinymce.urls')),
]
