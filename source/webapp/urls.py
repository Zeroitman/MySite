from django.urls import path
from webapp.views import ProgramList, ProgramDetailView, \
    SessionList, SessionDetailView, \
    SkillList, SkillDetailView, SkillUpdateView, SkillCreateView, delete_skill,\
    ResultList

app_name = 'webapp'


urlpatterns = [
    path('', SessionList.as_view(), name='session_list'),
    path('program/', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session_result/<int:pk>', ResultList.as_view(), name='session_result_view'),
    path('skill/', SkillList.as_view(), name='skill_list'),
    path('skill/<int:pk>', SkillDetailView.as_view(), name='skill_detail'),
    path('skill/create', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/update', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/<int:id>/delete', delete_skill, name='skill_delete'),
]




