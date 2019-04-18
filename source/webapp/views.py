from django.views.generic import ListView, DetailView
from webapp.models import Program, Session


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


class SessionDetail(DetailView):
    model = Session
    template_name = 'session_detail.html'





