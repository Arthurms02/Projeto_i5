from django.urls import path
from . import views

#urlpatterns
urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand-list'),
    path('brands/create/', views.BrandCreateView.as_view(), name='brand-create'),
    path('brands/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('brands/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand-delete'),

    path('api/v1/brands/', views.BrandCreateListAPIView.as_view(), name='brand-api'),
    path('api/v1/brands/<int:pk>/', views.BrandRetriverUpdateDestroyAPIView.as_view(), name='brand-api-detail'),
    path('api/v1/brands/<int:pk>/', views.BrandRetriverUpdateDestroyAPIView.as_view(), name='brand-api-update'),
    path('api/v1/brands/<int:pk>/', views.BrandRetriverUpdateDestroyAPIView.as_view(), name='brand-api-delete'),
]
