from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('<int:pk>/', views.record_detail, name='record_detail'),
    path('add_to_cart/<int:record_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('<int:record_id>/upload_image/', views.upload_image, name='upload_image'),
    path('success/', views.success_page, name='success_page')
] 