# product/views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from . models import Product, ProductImages, Category 
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.
def productlist(request, category_slug=None):
	# To get product by Category 
	category = None
	productlist  = Product.objects.all()
	categorylist = Category.objects.annotate(total_products=Count('product')) # total_products is based on the 'category rel with Product - One-to-Many'


	# To check if there is category slug
	if category_slug:
		# If there is, get the category slug objects and use 
		# them with category_slug
		# category = Category.objects.get(slug=category_slug)
		# NEW
		category = get_object_or_404(Category ,slug=category_slug)

		# Filter the products (productlist based on the category)
		productlist = productlist.filter(category=category)

	# # Search
	# search_query = request.GET.get('q')
	# if search_query:
	# 	print(search_query) 

	# # Search
	search_query = request.GET.get('q')
	if search_query:
		productlist = productlist.filter(
			Q(name__icontains = search_query) |
			Q(description__icontains = search_query) |
			Q(condition__icontains = search_query) |
			Q(brand__brand_name__icontains = search_query) |
			Q(category__category_name__icontains = search_query)
		) 



	# pagination
	paginator = Paginator(productlist, 2) # Show 25 contacts per page
	page = request.GET.get('page')
	productlist = paginator.get_page(page)	
	template = 'Product/product_list.html'

	context = {
		'product_list' : productlist, 
		'category_list': categorylist, 
		'category'     : category,}

	return render(request, template, context)


def productdetail(request, product_slug):
	
	## 4 STEPS TO LOAD AND DISPLAY THE INFORMATION FROM THE DB
	# 1. Get product by id from db
	productdetail = Product.objects.get(slug=product_slug)
	
	# NEW
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