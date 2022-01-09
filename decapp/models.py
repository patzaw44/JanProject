from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=44)
    model = models.CharField(max_length=44)

    def __str__(self):
        return self.make


class Rate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='new_rate')
    rating = models.IntegerField()

    # def __str__(self):
    #     return self.car_id
