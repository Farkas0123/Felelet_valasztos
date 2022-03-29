from django.db import models

class Kerdes(models.Model):
    hanyadik = models.IntegerField()
    kerdes = models.CharField(max_length=256)
    valasz1 = models.CharField(max_length=256)
    valasz2 = models.CharField(max_length=256)
    valasz3 = models.CharField(max_length=256)
    valasz4 = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Kérdés'
        verbose_name_plural = 'Kérdések'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"A kérdés {self.kerdes}"