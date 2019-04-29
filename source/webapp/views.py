from webapp.models import Program, Session, Result, Child
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import reverse
from webapp.forms import ChildForm, ResultForm
from django.urls import reverse_lazy


# ChildListView - главная страница с выводом детей
class ChildListView(ListView):
    model = Program
    template_name = 'child_list.html'


# ChildDetailView - страница просмотра профиля определенного ребенка
class ChildDetailView(DetailView):
    model = Child
    template_name = 'child_detail.html'


# ChildUpdateView - страница редактирования профиля ребенка
class ChildUpdateView(UpdateView):
    model = Child
    template_name = 'child_update.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


# ChildCreateView - страница добавления ребенка
class ChildCreateView(CreateView):
    model = Child
    template_name = 'child_create.html'
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
