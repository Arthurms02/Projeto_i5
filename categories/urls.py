from django.urls import path
from . import views

#urlpatterns
urlpatterns = [
    path('categoris/list/', views.CategoryListView.as_view(), name='categori-list'),
    path('categoris/create/', views.CategoryCreateView.as_view(), name='categori-create'),
    path('categoris/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='categori-detail'),
    path('categoris/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='categori-update'),
    path('categoris/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='categori-delete'),
]