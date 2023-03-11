from django.contrib import admin
from .models import Course, Chapter, Module, SubModule

admin.site.register([Course, Chapter, Module, SubModule])
