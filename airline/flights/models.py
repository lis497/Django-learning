from django.db import models

# Create your models here.
class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.city} ({self.code})"



class Flight(models.Model):
	#origin = models.CharField(max_length=64)
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, 
		                                related_name="departures")
	#models.CASCADE if delete one table, will delete other connected rows
	#models.PROTECT if you have other table connected, delete is not permit
	#related_name reverse engineering
	#destination = models.CharField(max_length=64)
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, 
		                                     related_name="arrivals")
	duration = models.IntegerField()

	def __str__(self):
		return f"{self.id}: {self.origin} --> {self.destination}"