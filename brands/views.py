from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models, forms, serializers
from rest_framework import generics


class BrandListView(LoginRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brands_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class BrandCreateView(LoginRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brands_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand-list')


class BrandDetailView(LoginRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brands_detail.html'
    context_object_name = 'brand'


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brands_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand-list')


class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brands_delete.html'
    success_url = reverse_lazy('brand-list')
    context_object_name = 'brand'


class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandRetriverUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer