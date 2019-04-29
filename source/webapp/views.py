from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Program, Session, Result, Skill
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import SkillForm
from django.urls import reverse, reverse_lazy


# SkillCreateView - страница со списком навыков
class SkillList(ListView):
    model = Skill
    template_name = 'skill_views/skill_list.html'


# SkillCreateView - страница деталей навыка
class SkillDetailView(DetailView):
    model = Skill
    template_name = 'skill_views/skill_detail.html'


# SkillCreateView - страница создания навыка
class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_create.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


# SkillUpdateView - страница редактирования навыка
class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_create.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


# SkillDeleteView - удаление навыка
def delete_skill(request, id):
    skill = get_object_or_404(Skill, pk=id)
    skill.delete()
    return redirect('webapp:skill_list')


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


class SessionList(ListView):
    model = Session
    template_name = 'session_list.html'


class ResultList(ListView):
    model = Result
    template_name = 'session_result.html'


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'


class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_detail.html'


# class SessionCreateView(CreateView):
#     form_class = SessionForm
#     template_name = 'session_create.html'
#     model = Session
#
#     def get_success_url(self):
#         return reverse('webapp:session_view', kwargs={'pk': self.object.pk})
