from django.shortcuts import render
from webapp.models import Program, Session
from django.views.generic import ListView, DetailView


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


def current_session(request, pk):
    current_program = Program.objects.get(id=pk)
    try:
        session, created_session = Session.objects.get_or_create(program=current_program)
        if created_session:
            session.save()
            return render(request, 'session_detail.html', {'program': current_program})
        else:
            return render(request, 'session_detail.html', {'program': current_program})
    except Exception as error:
        print("Error happened " + repr(error))


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'
