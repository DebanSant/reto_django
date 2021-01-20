from django.http import HttpResponse

def index(request):

    document='<h1>API - SISTEMA DE ENCUESTAS</h1><h3>&nbsp;TABLAS</h3><ul><li>USUARIOS</li><li>CATEGORIA&nbsp;&nbsp;</li><li>ENCUESTA (&nbsp; RELACI&Oacute;N MUCHOS A MUCHOS CON *ENCUESTAS * CATEGORIAS)<ul><li>PREGUNTAS ( RELACI&Oacute;N 1 A MUCHOS&nbsp; &nbsp;-&nbsp; 1 ENCUESTA&nbsp; -&nbsp; * PREGUNTAS)<ul><li>ALTERNATIVAS ( RELACI&Oacute;N 1 A MUCHOS -&nbsp; 1 PREgUNTA&nbsp; -&nbsp; * ALTERNATIVAS</li></ul></li></ul></li></ul><p>ENDPOINTS</p><p>Encuestas</p><h3><a title="Encuesta" href="/api/encuesta/">/api/encuesta/</a>----GET-POST</h3><h3><a title="Encuesta" href="/api/encuesta/1">/api/encuesta/id</a>----GET-PUT-DELETE</h3><p>Preguntas </p><h3><a title="Encuesta" href="/api/encuesta/1/pregunta">/api/encuesta/id/pregunta/</a>----GET-POST</h3><h3><a title="Encuesta" href="/api/encuesta/1/pregunta/1">/api/encuesta/id/pregunta/id</a>----GET-PUT-DELETE</h3><p>Alternativas</p><h3><a title="Encuesta" href="/api/encuesta/1/pregunta/1/alternativa">/api/encuesta/id/pregunta/id/alternativa</a>----GET-POST</h3><h3><a title="Encuesta" href="/api/encuesta/1/pregunta/1/alternativa/1">/api/encuesta/id/pregunta/id/alternativa/id</a>----GET-PUT-DELETE</h3>'

    return HttpResponse(document)
