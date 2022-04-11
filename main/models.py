from django.db import models
from django.utils.translation import get_language


class Restaurant(models.Model):
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    long = models.DecimalField(decimal_places=8, max_digits=11)
    lat = models.DecimalField(decimal_places=8, max_digits=11)
    start_at = models.TimeField()
    end_at = models.TimeField()
    photo = models.ImageField(default=None, blank=True, null=True)


    @property
    def name(self):
        return getattr(self, f"name_{get_language()}")

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT)
    name_uz = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(default=None, blank=True, null=True)

    @property
    def name(self):
        return getattr(self, f"name_{get_language()}")
