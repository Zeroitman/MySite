from webapp.models import Program
from django.views.generic import ListView, DetailView


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'
