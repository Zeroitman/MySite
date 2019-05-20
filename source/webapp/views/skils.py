from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Skill
from django.views.generic import DetailView, CreateView, UpdateView, View
from webapp.forms import SkillForm
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = 'skill_views/skill_detail.html'


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_create.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_update.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


def delete_skill(pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('webapp:categories_list')


class SkillSearchView(LoginRequiredMixin, View):
    template_name = 'skill_views/skill_search_results.html'

    def get(self):
        query = self.request.GET.get('q')
        searched_skills = Skill.objects.filter(
            Q(name__icontains=query) |
            Q(code_skill__icontains=query))
        context = {
            'searched_skills': searched_skills
        }
        return render(self.request, self.template_name, context)
