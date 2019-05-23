from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db import ProgrammingError
from webapp.models import Program, Session, Result, Skill, SkillsInProgram
from django.views.generic import CreateView
from webapp.forms import SkillsInProgramForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timezone
import threading
from django.contrib.auth.mixins import LoginRequiredMixin


def automatic_session_closure():
    threading.Timer(60, automatic_session_closure).start()
    now = datetime.now(timezone.utc)
    try:
        all_session = Session.objects.filter(status_session=False)
        for session in all_session:
            delta = now - session.created_date
            if delta.seconds > 7200:
                session.status_session = True
                session.save()
        automatic_program_closure()
    except ProgrammingError:
        print(ProgrammingError)


def automatic_program_closure():
    all_skills_in_program = SkillsInProgram.objects.all()
    number_of_program = []
    for skill in all_skills_in_program:
        number_of_program.append(skill.program.pk)
    i = 1
    if number_of_program:
        while i <= max(number_of_program):
            skills = SkillsInProgram.objects.filter(program_id=i)
            if skills:
                skills_in_the_program = []
                for skill in skills:
                    skills_in_the_program.append(skill.status)

                def find_all_closed_skills():
                    if skills_in_the_program[0]:
                        return False
                    first, *rest = skills_in_the_program
                    the_same = (x == first and x == False for x in rest)
                    return all(the_same)

                answer = find_all_closed_skills()
                if answer:
                    program = Program.objects.get(id=i)
                    program.status = False
                    program.save()
            i = i + 1


automatic_session_closure()


def create_session_and_result(request, pk):
    if request.user.is_authenticated:
        current_program = Program.objects.get(id=pk)
        skill_in_program = SkillsInProgram.objects.filter(program_id=current_program.pk, status=True)
        if not request.COOKIES.get("session_number"):
            session = Session.objects.create(program=current_program)
            session.save()
            for skill in skill_in_program:
                current_skill = SkillsInProgram.objects.get(pk=skill.pk)
                current_result = Session.objects.get(id=session.pk)
                result = Result.objects.create(skill=current_skill, session=current_result)
                result.save()

            response = render(request, 'session_views/session_detail.html',
                              {'list': skill_in_program, 'pk': session.pk, 'program': current_program,
                               'skills': Skill.objects.all()})
            response.set_cookie("session_number", session.pk, expires=7200)
            return response
        else:
            for skill in skill_in_program:
                current_skill = SkillsInProgram.objects.get(pk=skill.pk)
                current_result = Session.objects.get(id=request.COOKIES.get("session_number"))
                Result.objects.get_or_create(skill=current_skill, session=current_result)
            return render(request, 'session_views/session_detail.html',
                          {'list': skill_in_program, 'pk': request.COOKIES.get("session_number"),
                           'program': current_program,
                           'skills': Skill.objects.all()})
    else:
        return redirect('login')


class AddExtraSkill(LoginRequiredMixin, CreateView):
    model = SkillsInProgram
    form_class = SkillsInProgramForm

    def form_valid(self, form):
        form.instance.program = Program.objects.get(pk=self.kwargs.get('pk'))
        form.instance.status = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:session_create', kwargs={'pk': self.kwargs.get('pk')})


@csrf_exempt
def counter_done(request, pk):
    result = get_object_or_404(Result, skill=pk, session_id=request.COOKIES.get("session_number"))
    counter = request.POST.get('counter', None)
    result.done = int(counter)
    result.save()
    return JsonResponse({'counter': result.done})


@csrf_exempt
def counter_done_with_hint(request, pk):
    result = get_object_or_404(Result, skill=pk, session_id=request.COOKIES.get("session_number"))
    counter = request.POST.get('counter', None)
    result.done_with_hint = int(counter)
    result.save()
    return JsonResponse({'counter': result.done_with_hint})


def counter_get_view(request, pk):
    result = get_object_or_404(Result, skill=pk, session_id=request.COOKIES.get("session_number"))
    return JsonResponse({
        'result_done': result.done,
        'result_w_hint': result.done_with_hint,
        'total': result.total
    })
