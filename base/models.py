from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    registrationNumber = models.CharField(max_length=100)
    fuelType = models.CharField(max_length=50)

    driver = models.ForeignKey('auth.User', related_name='cars', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.model} - {self.registrationNumber.upper()}"


class CollectionPoint(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=20)
    telephoneNumber = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.city}"


class TestTube(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=500)
    color = models.CharField(max_length=50)
    transportTemperature = models.IntegerField()
    count = models.IntegerField()

    driver = models.ForeignKey('auth.User', related_name='testTubes', null=True, on_delete=models.SET_NULL)
    startPoint =  models.ForeignKey(CollectionPoint, related_name='ourTubes', on_delete=models.CASCADE)
    endPoint = models.ForeignKey(CollectionPoint, related_name='incomingTubes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shortName


