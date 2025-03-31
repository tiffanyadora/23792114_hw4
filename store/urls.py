from django.urls import path
from .views import home, product_detail, search, add_product_api, serve_csv

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_detail, name='product_detail'),    
    path('search/', search, name='search'),
    path('api/add-product/', add_product_api, name='add_product_api'),
    path("data/<str:filename>/", serve_csv, name="serve_csv"),
]