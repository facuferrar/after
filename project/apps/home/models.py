from django.db import models

class Modelo1(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()

class Modelo2(models.Model):
    campo3 = models.CharField(max_length=100)
    campo4 = models.IntegerField()

class Modelo3(models.Model):
    campo5 = models.CharField(max_length=100)
    campo6 = models.IntegerField()

class Modelo4(models.Model):
    campo7 = models.CharField(max_length=100)
    campo8 = models.IntegerField()
