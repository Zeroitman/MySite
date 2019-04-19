from django.shortcuts import render
from webapp.models import Program, Session
from django.views.generic import ListView, DetailView


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


def current_session(request, pk):
    current_program = Program.objects.get(id=pk)
    skill_ids_list = current_program.skill.all()
    skill_names_list = []
    session = Session.objects.create(program=current_program)
    session.save()
    for skill in skill_ids_list:
        skill_names_list.append(skill.name)
    return render(request, 'session_detail.html', {'list': skill_names_list, 'id': session.pk})


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'
