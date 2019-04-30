from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Program, Session, Result, Skill, Child
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from webapp.forms import SkillForm, ChildForm, ResultForm
from django.urls import reverse, reverse_lazy
from django.db.models import Q


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
    template_name = 'child_program_list.html'


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


# ChildList - страница выводящая список всех детей, без привязки к программе
class ChildList(ListView):
    model = Child
    template_name = 'child_views/child_list.html'


# ChildSearch - метод поиска по детям на странице детей, после отправки формы с именем либо фамилией ребенка
# Перекидывает на страницу child_search_results где подсчитывается количество результатов
# И все результаты в виде ListGroup(Bootstrap)
class ChildSearchView(View):
    template_name = 'child_views/child_search_results.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        # TODO сделать проверку на пустое поле, возможно сделать кнопку disabled при длине input'a <= 1.
        searched_child = Child.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(third_name__icontains=query) |
            Q(characteristic__icontains=query))
        # Q позволяет искать по полям из указанной переменной со всеми детьми в формате Q(__поле из модели Child/
        # __icontains=query)
        context = {
            'searched_child': searched_child
        }
        return render(self.request, self.template_name, context)
