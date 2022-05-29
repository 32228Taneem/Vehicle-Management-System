from django.db import models

# Create your models here.
class Vehicle(models.Model):
    name = models.CharField('Vehicle Name',max_length=120)
    brand = models.CharField('Brand Name',max_length=120)
    location = models.URLField(max_length=1000)
    speed = models.IntegerField("Speed")
    avg_speed = models.IntegerField("Average Speed")
    temperature = models.IntegerField("Tempearture")
    fuel_level = models.IntegerField("Fuel level")
    engine = models.IntegerField("Engine",blank=True,null=True)
    camera1 = models.URLField('Camera 1',max_length=1000)
    camera2 = models.URLField('Camera 2',max_length=1000)

    def __str__(self):
        return self.name