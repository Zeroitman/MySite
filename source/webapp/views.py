from webapp.models import Program, Session, Result
from django.views.generic import ListView, DetailView


# ChildList - главная страница с выводом детей
class ChildList(ListView):
    model = Program
    template_name = 'child_list.html'


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
