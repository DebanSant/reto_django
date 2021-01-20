from django.urls import path

from apps.encuesta.api.views.categoria_views import *
from apps.encuesta.api.views.encuesta_views import *
from apps.encuesta.api.views.pregunta_views import *
from apps.encuesta.api.views.alternativa_views import *
urlpatterns = [
    path('encuesta/',encuesta_api_view, name = 'encuesta_api_view'),
    path('encuesta/<int:pk>/',encuesta_detail_api_view, name = 'encuesta_detail_api_view'),

    path('categoria/', categoria_api_view, name='categoria_api_view'),
    path('categoria/<int:pk>/',categoria_detail_api_view,  name='categoria_detail_api_view'),

    path('encuesta/<int:pk_encuesta>/pregunta/', pregunta_api_view, name='pregunta_api_view'),
    path('encuesta/<int:pk_encuesta>/pregunta/<int:pk>/', pregunta_detail_api_view, name='pregunta_detail_api_view'),

    path('encuesta/<int:pk_encuesta>/pregunta/<int:pk_pregunta>/alternativa/', alternativa_api_view , name='alternativa_api_view'),
    path('encuesta/<int:pk_encuesta>/pregunta/<int:pk_pregunta>/alternativa/<int:pk_alternativa>', alternativa_detail_api_view, name='alternativa_detail_api_view'),

]
