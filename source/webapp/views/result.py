from django.shortcuts import get_object_or_404, redirect
from webapp.models import Program, Session, Result, SkillsInProgram
from django.views.generic import ListView, UpdateView
from webapp.forms import ResultForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from webapp.views.session import automatic_session_closure


class ResultListView(LoginRequiredMixin, ListView):
    model = Result
    template_name = 'session_views/session_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now_pk = int(self.kwargs.get('pk'))
        context['session_pk'] = now_pk
        current_session = Session.objects.get(id=now_pk)
        context['status_session'] = current_session.status_session
        context['date_of_session'] = current_session.created_date
        context['terapist'] = current_session.attending_therapist
        current_program = Program.objects.get(id=current_session.program_id)
        context['child'] = current_program.child
        return context

    def get_queryset(self):
        return Result.objects.filter(session=self.kwargs['pk'])


class ResultUpdateView(LoginRequiredMixin, UpdateView):
    model = Result
    form_class = ResultForm

    def get_success_url(self):
        return reverse('webapp:session_result_view',
                       kwargs={'pk': get_object_or_404(Result, pk=self.kwargs.get('pk')).session.pk})


def change_status_skill(request, pk):
    result = get_object_or_404(SkillsInProgram, pk=pk)
    session_pk = request.GET.get('session')
    result.status = False
    result.save()
    return redirect('webapp:session_result_view', pk=session_pk)


def close_session_result_view(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if session.status_session:
        automatic_session_closure()
        return redirect('webapp:program_detail', pk=session.program_id)
    else:
        session.status_session = True
        session.save()
        response = redirect('webapp:program_detail', pk=session.program_id)
        response.delete_cookie("session_number")
        automatic_session_closure()
        return response
