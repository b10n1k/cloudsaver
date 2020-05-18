from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from ideas import views
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ideas/', include('ideas.urls'), name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    #path('logout/', views.logout, name='logout'),
    path('', include('social_django.urls', namespace='social')),
    #path('tinymce/', include('tinymce.urls')),
    path('api', include('api.urls'), name='api'),
]
