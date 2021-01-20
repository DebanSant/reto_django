from django.db import models

# Create your models here.

class CategoriaEncuesta(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

class Encuesta(models.Model):
    name = models.CharField('Nombre de la Encuesta', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Descripción de la encuesta', blank=False, null=False)
    categories = models.ManyToManyField(CategoriaEncuesta)
    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'

    def __str__(self):
        return self.name

class Preguntas(models.Model):
    description = models.TextField('Descripción de la pregunta', blank=False, null=False)
    question_survey = models.ForeignKey(Encuesta, on_delete=models.CASCADE, verbose_name='Pregunta de la encuesta', null=True,related_name='preguntas')

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.description


class Alternativas(models.Model):
    description = models.TextField('Descripción de la alternativa', blank=False, null=False)
    alternative_question = models.ForeignKey(Preguntas, on_delete=models.CASCADE, verbose_name='Alternativa de la pregunta', null=True,related_name='alternativas')
    class Meta:
        verbose_name = 'Alternativa'
        verbose_name_plural = 'Alternativas'

    def __str__(self):
        return self.description