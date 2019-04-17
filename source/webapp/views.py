from django.views.generic.list import ListView
from webapp.models import Program


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


