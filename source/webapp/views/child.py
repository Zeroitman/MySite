from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Child
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.forms import ChildForm
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class ChildList(LoginRequiredMixin, ListView):
    queryset = Child.objects.active()
    model = Child
    template_name = 'child_views/child_list.html'


class ChildDetailView(LoginRequiredMixin, DetailView):
    model = Child
    template_name = 'child_views/child_detail.html'


class ChildUpdateView(LoginRequiredMixin, UpdateView):
    model = Child
    template_name = 'child_views/child_update.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


class ChildCreateView(LoginRequiredMixin, CreateView):
    model = Child
    template_name = 'child_views/child_create.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


def soft_delete_child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    child.is_deleted = True
    child.save()
    return redirect('webapp:child_list')


class ChildSearchView(LoginRequiredMixin, View):
    template_name = 'child_views/child_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_child = Child.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(third_name__icontains=query) |
            Q(characteristic__icontains=query))
        context = {
            'searched_child': searched_child
        }
        return render(self.request, self.template_name, context)
