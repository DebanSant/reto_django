from django.contrib import admin
from apps.encuesta.models import *


admin.site.register(CategoriaEncuesta)
admin.site.register(Encuesta)
admin.site.register(Preguntas)
admin.site.register(Alternativas)