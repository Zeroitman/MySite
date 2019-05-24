from django.shortcuts import render
from webapp.models import Program, Session, Result, SkillsInProgram, Skill
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.forms import ProgramForm
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class ChildInProgramListView(LoginRequiredMixin, ListView):
    model = Program
    template_name = 'program_views/child_program_list.html'


class ProgramListView(LoginRequiredMixin, ListView):
    model = Program
    template_name = 'program_views/program_list.html'


class ProgramDetailView(LoginRequiredMixin, DetailView):
    model = Program
    template_name = 'program_views/program_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now_pk = int(self.kwargs.get('pk'))
        open_skills = {}
        all_session_in_program = Session.objects.filter(program_id=now_pk, status_session=True)
        for session in all_session_in_program:
            all_true_skills = SkillsInProgram.objects.filter(program_id=now_pk, status=True)
            for skill_in_program in all_true_skills:
                current_program_skill = Result.objects.filter(session_id=session.pk, skill_id=skill_in_program)
                for skill_in_result in current_program_skill:
                    current_skill = Skill.objects.filter(id=skill_in_program.skill_id)
                    for skill in current_skill:
                        open_skills[skill.code_skill + " | " + skill.name] = str(skill_in_result.percent)
        context['all_skill'] = open_skills
        return context


class ProgramCreateView(LoginRequiredMixin, CreateView):
    model = Program
    template_name = 'program_views/program_create.html'
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('webapp:program_detail', kwargs={'pk': self.object.pk})


class ProgramUpdateView(LoginRequiredMixin, UpdateView):
    model = Program
    template_name = 'program_views/program_update.html'
    form_class = ProgramForm

    def form_valid(self, form):
        form.instance.program = Program.objects.get(pk=self.kwargs.get('pk'))
        if form.instance.status:
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:program_detail', kwargs={'pk': self.object.pk})


class ProgramSearchView(LoginRequiredMixin, View):
    template_name = 'program_views/program_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_program = Program.objects.filter(Q(name__icontains=query))
        context = {
            'searched_program': searched_program
        }
        return render(self.request, self.template_name, context)
