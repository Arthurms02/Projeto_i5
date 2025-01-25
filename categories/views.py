from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import models, forms


class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = 'categoris_list.html'
    context_object_name = 'categoris'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(title__icontains=name)

        return queryset


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Category
    template_name = 'categoris_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('categori-list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = models.Category
    template_name = 'categoris_detail.html'
    context_object_name = 'categori'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'categoris_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('categori-list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'categoris_delete.html'
    success_url = reverse_lazy('categori-list')
    context_object_name = 'categori'

