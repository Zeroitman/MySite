from django.shortcuts import render
from webapp.models import Program, Session
from django.views.generic import ListView, DetailView, CreateView
from webapp.forms import SessionForm
from django.urls import reverse



class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


class SessionList(ListView):
    model = Session
    template_name = 'session_list.html'


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'


class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_detail.html'


class SessionCreateView(CreateView):
    form_class = SessionForm
    template_name = 'session_create.html'
    model = Session

    def get_success_url(self):
        return reverse('webapp:session_view', kwargs={'pk': self.object.pk})
