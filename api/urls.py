from django.urls import path, include
from . import views
from rest_framework import routers


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ideas', views.IdeaViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
