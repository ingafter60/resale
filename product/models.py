# product/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# model name: Category
class Category(models.Model):
	
	## It contains information about product Category
	category_name 	= models.CharField(max_length=50)
	image 			= models.ImageField(upload_to='category/', blank=True, null=True)
	
	# Add slug line: 15-20
	slug 			= models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug and self.category_name:
			self.slug = slugify(self.category_name)
		super(Category, self).save(*args, **kwargs)	

	## Making correct plural of 'Categorys' to 'Categories'
	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.category_name	


# model name: Product
class Product(models.Model):

	## Each product has its own condition (new or used)
	CONDITION_TYPE = (
		("New", "New"),
		("Used", "Used")
	)

	## It contains all the products information
	name 			= models.CharField(max_length=100)
	owner 		= models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=500)
	condition 	= models.CharField(max_length=100, choices=CONDITION_TYPE)
	category 	= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	brand 		= models.ForeignKey('Brand' , on_delete=models.SET_NULL, null=True)
	price 		= models.DecimalField(max_digits=10, decimal_places=2)
	image 		= models.ImageField(upload_to='main_product/', blank=True, null=True)
	created 		= models.DateTimeField(default=timezone.now)
	slug 			= models.SlugField(blank=True, null=True)

	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)	

	def __str__(self):
		return self.name



# model name: Brand
class Brand(models.Model):
    ## for product brand
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name	


# model name: ProductImages
class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    image 	= models.ImageField(upload_to='products/', blank=True , null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'        

    def __str__(self):
        return self.product.name







'''
PRODUCT
=======

1NF: Product
------------
name, description, condition, price, published

2NF: Product
------------
name, description, condition(new, used), price, published

3NF: Product
------------
name, owner, description, condition(new, used), price, published

4NF: Product
------------
name, owner, description, condition(new, used), price, published(add time saving)


CATEGORY
========

1NF: Category
------------
name, image




'''
