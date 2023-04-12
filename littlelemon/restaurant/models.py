from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=200)
    guests = models.IntegerField()
    reservation_date = models.DateField()

    def __str__(self):
        return self.name
