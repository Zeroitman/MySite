from webapp.models import Program, Session
from django.views.generic import ListView, DetailView


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


class SessionDetail(DetailView):
    model = Session
    template_name = 'session_detail.html'


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'
