# src/config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('products/', include('product.urls', namespace='products')),
   path('admin/', admin.site.urls),
] 
# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Serving files uploaded by a user during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
