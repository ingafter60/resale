# product/views.py
from django.shortcuts import render
from . models import Product, ProductImages 

# Create your views here.
def productlist(request):
	
	## 4 STEPS TO LOAD AND DISPLAY THE INFORMATION FROM THE DB
	# 1. Get all products from db
	productlist = Product.objects.all()
	# test
	# print(productlist)
	# result: <QuerySet [<Product: Lenovo A588T>, <Product: iPhone 11 Pro>]>
	# 2. Template to render
	template = 'Product/product_list.html'	
	# 3. Store the information in variable context
	context = {'product_list': productlist}
	# 4. Render the informatio to template
	return render(request, template, context)


def productdetail(request, product_slug):
	
	## 4 STEPS TO LOAD AND DISPLAY THE INFORMATION FROM THE DB
	# 1. Get product by id from db
	productdetail = Product.objects.get(slug=product_slug)
	# test
	print(product_slug)
	# result: <QuerySet [<Product: Lenovo A588T>, <Product: iPhone 11 Pro>]>
	productimages = ProductImages.objects.filter(product=productdetail)
	# 2. Template to render
	template = 'Product/product_detail.html'	
	# 3. Store the information in variable context
	context = {'product_detail': productdetail, 'product_images' : productimages}
	# 4. Render the informatio to template
	return render(request, template, context)