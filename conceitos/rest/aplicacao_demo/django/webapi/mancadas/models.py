from django.db import models


class Individuo(models.Model):
    nome = models.CharField(max_length=50)
    cafe_com_leite = models.BooleanField(default=False)


class Mancada(models.Model):
    individuo = models.ForeignKey('mancadas.Individuo', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    mancada = models.TextField()
    perdoada = models.BooleanField(default=False)
