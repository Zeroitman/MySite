from django.shortcuts import render
from webapp.models import Program, Session
from django.views.generic import ListView, DetailView, CreateView
from webapp.forms import SessionForm
from django.urls import reverse


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


# def current_session(request, pk):
#     current_program = Program.objects.get(id=pk)
#     try:
#         session, created_session = Session.objects.get_or_create(program=current_program)
#         if created_session:
#             session.save()
#             return render(request, 'session_detail.html', {'program': current_program})
#         else:
#             return render(request, 'session_detail.html', {'program': current_program})
#     except Exception as error:
#         print("Error happened " + repr(error))


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'


class SessionCreateView(CreateView):
    form_class = SessionForm
    template_name = 'session_create.html'
    model = Session

    def get_success_url(self):
        return reverse('webapp:session_view', kwargs={'pk': self.object.pk})
