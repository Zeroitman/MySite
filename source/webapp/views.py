from webapp.models import Program, Session, Result, Child
from django.views.generic import ListView, DetailView


# ChildList - главная страница с выводом детей
class ChildList(ListView):
    model = Program
    template_name = 'child_list.html'


# ChildDetail - страница просмотра профиля определенного ребенка
class ChildDetail(DetailView):
    model = Child
    template_name = 'child_detail.html'


# ProgramList - страница вывода всех программ
class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


# ProgramDetail - страница просмотра деталей определенной программы
class ProgramDetail(DetailView):
    model = Program
    template_name = 'program_detail.html'


# ResultList - страница вывода результатов сессий
class ResultList(ListView):
    model = Result
    template_name = 'session_result.html'


# SessionDetailView - страница просмотра делатей
class SessionDetail(DetailView):
    model = Session
    template_name = 'session_detail.html'
