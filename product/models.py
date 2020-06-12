# product/models.py
from django.db import models

# model name: Product
class Product(models.Model):

	## Each product has its own condition (new or used)
	CONDITION_TYPE = (
		("New", "New"),
		("Used", "Used")
	)

	## It contains all the products information
	name 			= models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	condition 	= models.CharField(max_length=100, choices=CONDITION_TYPE)
	price 		= models.DecimalField(max_digits=10, decimal_places=2)
	created 		= models.DateTimeField()

	def __str__(self):
		return self.name














'''
1NF: Product
============
name, description, condition, price, published

2NF: Product
============
name, description, condition(new, used) price, published









'''
