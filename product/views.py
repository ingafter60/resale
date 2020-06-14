# product/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from . models import Product, ProductImages, Category 
from django.db.models import Count

# Create your views here.
def productlist(request):
	
	## 4 STEPS TO LOAD AND DISPLAY THE INFORMATION FROM THE DB
	# 1. Get all products from db
	productlist  = Product.objects.all()
	# categorylist = Category.objects.all()
	categorylist = Category.objects.annotate(total_products=Count('product')) # total_products is based on the 'category rel with Product - One-to-Many'
	# test
	# print(productlist)
	# result: <QuerySet [<Product: Lenovo A588T>, <Product: iPhone 11 Pro>]>
	# 2. Template to render
	template = 'Product/product_list.html'
	
	# pagination
	paginator = Paginator(productlist, 2) # Show 25 contacts per page
	page = request.GET.get('page')
	productlist = paginator.get_page(page)	

	# 3. Store the information in variable context
	context = {'product_list': productlist, 'category_list': categorylist}
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

def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'list.html', {'contacts': contacts})	