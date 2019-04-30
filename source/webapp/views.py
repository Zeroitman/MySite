from webapp.models import Program, Session, Result, Child
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.db.models import Q


# ChildList - главная страница с выводом детей
class ChildProgramList(ListView):
    model = Program
    template_name = 'child_program_list.html'


# ProgramList - страница вывода всех программ
class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


# ResultList - страница вывода результатов сессий
class ResultList(ListView):
    model = Result
    template_name = 'session_result.html'


# ProgramDetail - страница просмотра деталей определенной программы
class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'


# SessionDetailView - страница просмотра делатей
class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_detail.html'


# ChildList - страница выводящая список всех детей, без привязки к программе
class ChildList(ListView):
    model = Child
    template_name = 'child_list.html'


# ChildSearch - метод поиска по детям на странице детей, после отправки формы с именем либо фамилией ребенка
# Перекидывает на страницу child_search_results где подсчитывается количество результатов
# И все результаты в виде ListGroup(Bootstrap)
class ChildSearchView(View):
    template_name = 'child_search_results.html'

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
