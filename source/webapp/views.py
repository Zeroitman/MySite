from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from webapp.models import Program, Session, Result
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse


class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'


class SessionList(ListView):
    model = Session
    template_name = 'session_list.html'


class ResultList(ListView):
    model = Result
    template_name = 'session_result.html'


class ProgramDetailView(DetailView):
    model = Program
    template_name = 'program_detail.html'


class SessionDetailView(DetailView):
    model = Session
    template_name = 'session_detail.html'


# Вьюшки счетчика, сохранение результатов накликивания, связано с фронтендом


def counter_done(request, pk):
    result = get_object_or_404(Result, skill=pk)
    counter = request.POST.get('counter', None)
    result.done = counter
    result.save()
    return JsonResponse({'counter': result.done})


def counter_done_with_hint(request, pk):
    result = get_object_or_404(Result, skill=pk)
    counter = request.POST.get('counter', None)
    result.done_with_hint = counter
    result.save()
    return JsonResponse({'counter': result.done_with_hint})
