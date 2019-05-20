from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Categories
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.forms import CategoryForm
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Categories
    template_name = 'category_views/categories_list.html'


class CategoriesDetailView(LoginRequiredMixin, DetailView):
    model = Categories
    template_name = 'category_views/categories_detail.html'


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'category_views/categories_create.html'

    def get_success_url(self):
        return reverse('webapp:categories_list')


class CategoriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Categories
    template_name = 'category_views/categories_update.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('webapp:categories_list')


def delete_category(pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('webapp:categories_list')


class CategoriesSearchView(LoginRequiredMixin, View):
    template_name = 'category_views/categories_search_results.html'

    def get(self):
        query = self.request.GET.get('q')
        searched_categories = Categories.objects.filter(
            Q(name__icontains=query) |
            Q(code_category__icontains=query))
        context = {
            'searched_categories': searched_categories
        }
        return render(self.request, self.template_name, context)
