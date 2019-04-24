from django.shortcuts import render
from webapp.models import Program, Session
from django.views.generic import ListView, DetailView, FormView


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



class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'

    #
    # def get_queryset(self):
    #     program_keywords = self.request.GET.get('program_keywords')
    #     if program_keywords:
    #         return self.model.objects.filter(title__icontains=program_keywords) \
    #            | self.model.objects.filter(text__icontains=program_keywords)
    #     else:
    #         return self.model.objects.all()

