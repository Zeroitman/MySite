from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from mysql.connector import MySQLConnection
from webapp.models import Program, Session, Result, Skill, Child, Categories, SkillsInProgram
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from webapp.forms import SkillForm, ChildForm, ResultForm, ProgramForm, CategoryForm, SkillsInProgramForm
from django.urls import reverse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timezone
import threading
from django.contrib.auth.mixins import LoginRequiredMixin


def automatic_session_closure():
    threading.Timer(60, automatic_session_closure).start()
    now = datetime.now(timezone.utc)
    conn = MySQLConnection(user='aba_django', password='aba_django', host='127.0.0.1', database='ABA')
    cursor = conn.cursor()
    stmt = "SHOW TABLES WHERE `Tables_in_ABA` LIKE 'webapp_session%' OR `Tables_in_ABA` LIKE 'webapp_skillsinprogram%';"
    cursor.execute(stmt)
    if cursor.fetchone():
        automatic_program_closure()
        all_session = Session.objects.filter(status_session=False)
        for session in all_session:
            delta = now - session.created_date
            if delta.seconds > 7200:
                session.status_session = True
                session.save()


def automatic_program_closure():
    all_skills_in_program = SkillsInProgram.objects.all()
    number_of_program = []
    for skill in all_skills_in_program:
        number_of_program.append(skill.program.pk)
    i = 1
    if number_of_program:
        while i <= max(number_of_program):
            skills = SkillsInProgram.objects.filter(program_id=i)
            skills_in_the_program = []
            for skill in skills:
                skills_in_the_program.append(skill.status)

            def find_all_closed_skills():
                if not skills_in_the_program:
                    return True
                first, *rest = skills_in_the_program
                the_same = (x == first and False for x in rest)
                return all(the_same)

            answer = find_all_closed_skills()
            if answer:
                program = Program.objects.get(id=i)
                program.status = False
                program.save()
            i = i + 1


automatic_session_closure()


# Skill-----------------------------------------------------------------------------------------------------------------
class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    template_name = 'skill_views/skill_detail.html'


class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_create.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skill_views/skill_update.html'

    def get_success_url(self):
        return reverse('webapp:skill_detail', kwargs={'pk': self.object.pk})


def delete_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('webapp:categories_list')


class SkillSearchView(LoginRequiredMixin, View):
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
class ChildList(LoginRequiredMixin, ListView):
    # Query с детьми со статусом active, active берется из менеджера в моделях.
    queryset = Child.objects.active()
    model = Child
    template_name = 'child_views/child_list.html'


class ChildDetailView(LoginRequiredMixin, DetailView):
    model = Child
    template_name = 'child_views/child_detail.html'


class ChildUpdateView(LoginRequiredMixin, UpdateView):
    model = Child
    template_name = 'child_views/child_update.html'
    form_class = ChildForm

    def get_success_url(self):
        return reverse('webapp:child_detail', kwargs={'pk': self.object.pk})


class ChildCreateView(LoginRequiredMixin, CreateView):
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


class ChildSearchView(LoginRequiredMixin, View):
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
        all_true_skills = SkillsInProgram.objects.filter(program_id=now_pk, status=True)
        all_session_in_program = Session.objects.filter(program_id=now_pk, status_session=True)
        skills = {}
        for session in all_session_in_program:
            for sk in all_true_skills:
                current_program_skill = Result.objects.filter(session_id=session.pk, skill_id=sk)
                for skill in current_program_skill:
                    skills[skill.skill_id] = str(skill.percent)
        context['all_skill'] = skills
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


class AddExtraSkill(LoginRequiredMixin, CreateView):
    model = SkillsInProgram
    form_class = SkillsInProgramForm

    def form_valid(self, form):
        form.instance.program = Program.objects.get(pk=self.kwargs.get('pk'))
        form.instance.status = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:session_create', kwargs={'pk': self.kwargs.get('pk')})


# Result----------------------------------------------------------------------------------------------------------------
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


# Session---------------------------------------------------------------------------------------------------------------
class SessionDetailView(LoginRequiredMixin, DetailView):
    model = Session
    template_name = 'session_views/session_detail.html'


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


# Categories------------------------------------------------------------------------------------------------------------
class CategoriesListView(LoginRequiredMixin, ListView):
    model = Categories
    template_name = 'category_views/categories_list.html'


class CategoriesDetailView(LoginRequiredMixin, DetailView):
    model = Categories
    template_name = 'category_views/categories_detail.html'


class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'category_views/categories_create.html'

    def get_success_url(self):
        return reverse('webapp:categories_list')


class CategoriesUpdateView(LoginRequiredMixin, UpdateView):
    model = Categories
    template_name = 'category_views/categories_update.html'
    form_class = CategoryForm

    def get_success_url(self):
        return reverse('webapp:categories_list')


def delete_category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('webapp:categories_list')


class CategoriesSearchView(LoginRequiredMixin, View):
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
