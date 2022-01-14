from django.urls import path,include

from . import views
app_name = 'store'

urlpatterns = [
    path('', views.all_product, name='all_product'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
     path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]