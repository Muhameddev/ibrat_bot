from django.db import models




class Nom(models.Model):
    til = models.CharField(max_length=200)

    def __str__(self):
        return self.til

class Video(models.Model):
    til = models.ForeignKey(Nom,on_delete=models.CASCADE)
    nomer = models.BigIntegerField()
    holati = models.CharField(max_length=2000,default="Gramatika")
    link = models.CharField(max_length=10000)

    def __str__(self):
        return f"{Nom.til}:\n{self.nomer}-dars"

