from django.urls import path
from . import views

#urlpatterns
urlpatterns = [
    path('products/list/', views.ProductListView.as_view(), name='product-list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),

    path('api/v1/products/', views.ProductCreatedListAPIView.as_view(), name='product-api'),
    path('api/v1/products/', views.ProductRetriverUpdateDestroyAPIView.as_view(), name='product-api-detail'),
    path('api/v1/products/', views.ProductRetriverUpdateDestroyAPIView.as_view(), name='product-api-update'),
    path('api/v1/products/', views.ProductRetriverUpdateDestroyAPIView.as_view(), name='product-api-delete'),
]
