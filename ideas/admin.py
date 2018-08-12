from django.contrib import admin

# Register your models here.
from .models import Idea, Ideas_Group

admin.site.register(Idea)
admin.site.register(Ideas_Group)
