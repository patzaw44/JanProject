from django.db import models


class Auto(models.Model):
    make = models.CharField(max_length=44)
    model = models.CharField(max_length=44)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    rates_number = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.make)


class NewRate(models.Model):
    rating = models.IntegerField(default=5, null=True)
    car_rate = models.ForeignKey(Auto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.car_rate)
