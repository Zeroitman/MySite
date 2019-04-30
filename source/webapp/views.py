from django.shortcuts import get_object_or_404, redirect
from webapp.models import Program, Session, Result, Skill, Child
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import SkillForm, ChildForm, ResultForm
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
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('webapp:skill_list')


# ChildListView - главная страница с выводом детей
class ChildListView(ListView):
    model = Program
    template_name = 'child_list.html'


# ChildDetailView - страница просмотра профиля определенного ребенка
class ChildDetailView(DetailView):
    model = Child
    template_name = 'child_views/child_detail.html'


# ChildUpdateView - страница редактирования профиля ребенка
class ChildUpdateView(UpdateView):
    model = Child
    template_name = 'child_views/child_update.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


# ChildCreateView - страница добавления ребенка
class ChildCreateView(CreateView):
    model = Child
    template_name = 'child_views/child_create.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


# ChildDeleteView- страница удаления ребенка
class ChildDeleteView(DeleteView):
    model = Child
    success_url = reverse_lazy('webapp:child_list')


# ProgramListView - страница вывода всех программ
class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'


# ProgramDetailView - страница просмотра деталей определенной программы
class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'


# ResultListView - страница вывода результатов сессий
class ResultListView(ListView):
    model = Result
    template_name = 'session_result.html'


# ResultUpdateView - страница изменения результатов сессий
class ResultUpdateView(UpdateView):
    model = Result
    template_name = 'result_update.html'
    form_class = ResultForm

    # success_url = reverse_lazy('webapp:child_list')

    def get_success_url(self):
        return reverse('webapp:session_result_view', kwargs={'pk': self.object.pk})


# SessionDetailView - страница просмотра делатей
class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_detail.html'
