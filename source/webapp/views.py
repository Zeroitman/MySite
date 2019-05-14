from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Program, Session, Result, Skill, Child, Categories, SkillsInProgram
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.forms import SkillForm, ChildForm, ResultForm, ProgramForm, CategoryForm, SkillsInProgramForm
from django.urls import reverse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timezone
import threading


def automatic_session_and_program_closure():
    threading.Timer(60, automatic_session_and_program_closure).start()
    now = datetime.now(timezone.utc)
    all_session = Session.objects.filter(status_session=False)
    for session in all_session:
        delta = now - session.created_date
        if delta.seconds > 7200:
            session.status_session = True
            session.save()
    all_skills_in_program = SkillsInProgram.objects.all()
    d = []
    for skill in all_skills_in_program:
        d.append(skill.program.pk)
    i = 1
    while i <= max(d):
        skills = SkillsInProgram.objects.filter(program_id=i)
        e = []
        for a in skills:
            e.append(a.status)

        def all_the_same():
            if not e:
                return True
            first, *rest = e
            the_same = (x == first and x == False for x in rest)
            return all(the_same)

        a = all_the_same()
        if a:
            program = Program.objects.get(id=i)
            program.status = False
            program.save()
        i = i + 1


automatic_session_and_program_closure()


# Skill-----------------------------------------------------------------------------------------------------------------
class SkillDetailView(DetailView):
    model = Skill
    template_name = 'skill_views/skill_detail.html'


class SkillCreateView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_create.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


class SkillUpdateView(UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_update.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('webapp:categories_list')


class SkillSearchView(View):
    template_name = 'skill_views/skill_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_skills = Skill.objects.filter(
            Q(name__icontains=query) |
            Q(code_skill__icontains=query))
        context = {
            'searched_skills': searched_skills
        }
        return render(self.request, self.template_name, context)


# Child-----------------------------------------------------------------------------------------------------------------
class ChildList(ListView):
    # Query с детьми со статусом active, active берется из менеджера в моделях.
    queryset = Child.objects.active()
    model = Child
    template_name = 'child_views/child_list.html'


class ChildDetailView(DetailView):
    model = Child
    template_name = 'child_views/child_detail.html'


class ChildUpdateView(UpdateView):
    model = Child
    template_name = 'child_views/child_update.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


class ChildCreateView(CreateView):
    model = Child
    template_name = 'child_views/child_create.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


# Мягкое удаление, статус ребенка при удалении переводится в False.
def soft_delete_child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    child.is_deleted = True
    child.save()
    return redirect('webapp:child_list')


class ChildSearchView(View):
    template_name = 'child_views/child_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_child = Child.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(third_name__icontains=query) |
            Q(characteristic__icontains=query))
        context = {
            'searched_child': searched_child
        }
        return render(self.request, self.template_name, context)


# Program---------------------------------------------------------------------------------------------------------------
class ChildInProgramListView(ListView):
    model = Program
    template_name = 'program_views/child_program_list.html'


class ProgramListView(ListView):
    model = Program
    template_name = 'program_views/program_list.html'


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_views/program_detail.html'


class ProgramCreateView(CreateView):
    model = Program
    template_name = 'program_views/program_create.html'
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('webapp:program_detail', kwargs={'pk': self.object.pk})


class ProgramUpdateView(UpdateView):
    model = Program
    template_name = 'program_views/program_update.html'
    form_class = ProgramForm

    def get_success_url(self):
        return reverse('webapp:program_detail', kwargs={'pk': self.object.pk})


class ProgramSearchView(View):
    template_name = 'program_views/program_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_program = Program.objects.filter(Q(name__icontains=query))
        context = {
            'searched_program': searched_program
        }
        return render(self.request, self.template_name, context)


class AddExtraSkill(CreateView):
    model = SkillsInProgram
    form_class = SkillsInProgramForm

    def form_valid(self, form):
        form.instance.program = Program.objects.get(pk=self.kwargs.get('pk'))
        form.instance.status = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:session_create', kwargs={'pk': self.kwargs.get('pk')})


# Result----------------------------------------------------------------------------------------------------------------
class ResultListView(ListView):
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


class ResultUpdateView(UpdateView):
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


# Session---------------------------------------------------------------------------------------------------------------
class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_views/session_detail.html'


def create_session_and_result(request, pk):
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
        response.set_cookie("session_number", session.pk)
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


def change_status_session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    if session.status_session:
        response = HttpResponseRedirect('http://localhost:8000/program/' + str(session.program_id))
        response.delete_cookie("session_number")
        automatic_session_and_program_closure()
        return response
    else:
        session.status_session = True
        session.save()
        response = HttpResponseRedirect('http://localhost:8000/program/' + str(session.program_id))
        response.delete_cookie("session_number")
        automatic_session_and_program_closure()
        return response


# Categories------------------------------------------------------------------------------------------------------------
class CategoriesListView(ListView):
    model = Categories
    template_name = 'category_views/categories_list.html'


class CategoriesDetailView(DetailView):
    model = Categories
    template_name = 'category_views/categories_detail.html'


class CategoriesCreateView(CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'category_views/categories_create.html'

    def get_success_url(self):
        return reverse('webapp:categories_list')


class CategoriesUpdateView(UpdateView):
    model = Categories
    template_name = 'category_views/categories_update.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('webapp:categories_list')


def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('webapp:categories_list')


class CategoriesSearchView(View):
    template_name = 'category_views/categories_search_results.html'

    def get(self, request):
        query = self.request.GET.get('q')
        searched_categories = Categories.objects.filter(
            Q(name__icontains=query) |
            Q(code_category__icontains=query))
        context = {
            'searched_categories': searched_categories
        }
        return render(self.request, self.template_name, context)


# Вьюшки счетчика, сохранение результатов накликивания, связано с фронтендом--------------------------------------------
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
