from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class spidershot_Speed(models.Model):
    class Meta:
        verbose_name = _("SpiderShot")
    date = models.DateField(auto_now=True)
    accuracy = models.PositiveIntegerField(null=True, verbose_name = "Précision")
    targets = models.PositiveIntegerField(verbose_name = "Nombre de cibles")
    hits = models.PositiveIntegerField(verbose_name = "Nombre de cibles touchées")
    reaction = models.PositiveIntegerField(verbose_name = "Temps de réaction")

class strafetrack_Precision(models.Model):
    date = models.DateField(auto_now=True)
    accuracy = models.PositiveIntegerField(null=True, verbose_name = "Précision")
    average_t_on_t = models.PositiveIntegerField(verbose_name = "Temps moyen sur la cible")

class freetrack(models.Model):
    date = models.DateField(auto_now=True)
    accuracy = models.PositiveIntegerField(null=True, verbose_name = "Précision")
    hits = models.PositiveIntegerField(verbose_name = "Nombre de cibles touchées")
    headshots = models.PositiveIntegerField(verbose_name = "Tirs dans la tête")

class multishot(models.Model):
    date = models.DateField(auto_now=True)
    accuracy = models.PositiveIntegerField(null=True, verbose_name = "Précision")
    kill_per_second = models.PositiveIntegerField(null = True, verbose_name = "K/S")

class list(models.Model):
    nom = models.CharField(max_length=1000)