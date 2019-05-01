from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Program, Session, Result, Skill, Child, Categories
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from webapp.forms import SkillForm, ChildForm, ResultForm, ProgramForm
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
    template_name = 'skill_views/skill_update.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


# SkillDeleteView - удаление навыка
def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('webapp:skill_list')


# ChildList - страница выводящая список всех детей, без привязки к программе
class ChildList(ListView):
    model = Child
    template_name = 'child_views/child_list.html'


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


# ChildSearch - метод поиска по детям на странице детей, после отправки формы с именем либо фамилией ребенка
# Перекидывает на страницу child_search_results где подсчитывается количество результатов
# И все результаты в виде ListGroup(Bootstrap)
class ChildSearchView(View):
    template_name = 'child_views/child_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
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


# ChildInProgramListView - главная страница с выводом детей c программами
class ChildInProgramListView(ListView):
    model = Program
    template_name = 'program_views/child_program_list.html'


# ProgramListView - страница вывода всех программ
class ProgramListView(ListView):
    model = Program
    template_name = 'program_views/program_list.html'


# ProgramDetailView - страница просмотра деталей определенной программы
class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_views/program_detail.html'


# ProgramCreateView - страница добавления ребенка
class ProgramCreateView(CreateView):
    model = Program
    template_name = 'program_views/program_create.html'
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('webapp:program_detail', kwargs={'pk': self.object.pk})


# ProgramUpdateView - страница просмотра деталей определенной программы
class ProgramUpdateView(UpdateView):
    model = Program
    template_name = 'program_views/program_update.html'
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('webapp:program_detail', kwargs={'pk': self.object.pk})


# ProgramSearch - метод поиска по программа на странице програм, после отправки формы с именем программы
class ProgramSearchView(View):
    template_name = 'program_views/program_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_program = Program.objects.filter(Q(name__icontains=query))
        context = {
            'searched_program': searched_program
        }
        return render(self.request, self.template_name, context)


# ResultListView - страница вывода результатов сессий
class ResultListView(ListView):
    model = Result
    template_name = 'session_views/session_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session_pk'] = self.kwargs.get('pk')
        return context

    def get_queryset(self):
        return Result.objects.filter(session=self.kwargs['pk'])


# ResultUpdateView - страница изменения результатов сессий
class ResultUpdateView(UpdateView):
    model = Result
    form_class = ResultForm

    def get_success_url(self):
        return reverse('webapp:session_result_view',
                       kwargs={'pk': get_object_or_404(Result, pk=self.kwargs.get('pk')).session.pk})


# SessionDetailView - страница просмотра делатей
class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_views/session_detail.html'


# Вьюшки счетчика, сохранение результатов накликивания, связано с фронтендом
def counter_done(request, pk):
    result = get_object_or_404(Result, skill=pk)
    counter = request.POST.get('counter', None)
    result.done = int(counter)
    result.save()
    return JsonResponse({'counter': result.done})


def counter_done_with_hint(request, pk):
    result = get_object_or_404(Result, skill=pk)
    counter = request.POST.get('counter', None)
    result.done_with_hint = int(counter)
    result.save()
    return JsonResponse({'counter': result.done_with_hint})


# Список категорий
class CategoriesListView(ListView):
    model = Categories
    template_name = 'categories_list.html'
