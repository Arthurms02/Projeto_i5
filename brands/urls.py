from django.urls import path
from . import views

#urlpatterns
urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brand-list'),
    path('brand/create/', views.BrandCreateView.as_view(), name='brand-create'),
    path('brand/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand-detail'),
    path('brand/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand-update'),
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand-delete'),
]
