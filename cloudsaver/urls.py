from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ideas/', include('ideas.urls')),
    path('admin/', admin.site.urls),
]
