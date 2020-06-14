# product/urls.py
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
	# path for product list 
	path('', views.productlist, name='product_list'),
	# path for product by category
	path('<slug:category_slug>', views.productlist, name='product_list_category'),
	# path for product detail
	path('<slug:product_slug>', views.productdetail, name='product_detail'),
] 









