from django.urls import path
from webapp.views import \
    ProgramDetailView, ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramSearchView, ChildInProgramListView, \
    ChildList, ChildSearchView, ChildDetailView, ChildUpdateView, ChildCreateView, soft_delete_child, \
    SessionDetailView, counter_done_with_hint, counter_done, create_session_and_result, \
    SkillDetailView, SkillUpdateView, SkillCreateView, SkillSearchView, delete_skill, \
    ResultUpdateView, ResultListView, \
    CategoriesListView, CategoriesDetailView, CategoriesCreateView, CategoriesUpdateView, CategoriesSearchView, \
    delete_category \

app_name = 'webapp'

urlpatterns = [
    # counter urls------------------------------------------------------------------------------------------------
    path('skill_w_hint/<int:pk>', counter_done_with_hint, name='done_w_hint'),
    path('skill_done/<int:pk>', counter_done, name='counter_done'),
    # child urls--------------------------------------------------------------------------------------------------
    path('child/', ChildList.as_view(), name='child_list'),
    path('child_search/', ChildSearchView.as_view(), name='search_view'),
    path('child/<int:pk>', ChildDetailView.as_view(), name='child_detail'),
    path('child/create', ChildCreateView.as_view(), name='child_create'),
    path('child/<int:pk>/update', ChildUpdateView.as_view(), name='child_update'),
    path('child/<int:pk>/delete', soft_delete_child, name='child_delete'),
    # program urls------------------------------------------------------------------------------------------------
    path('', ChildInProgramListView.as_view(), name='child_program_list'),
    path('program/', ProgramListView.as_view(), name='program_list'),
    path('program_search/', ProgramSearchView.as_view(), name='search_view_program'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('program/create', ProgramCreateView.as_view(), name='program_create'),
    path('program/<int:pk>/update', ProgramUpdateView.as_view(), name='program_update'),
    # category urls-----------------------------------------------------------------------------------------------
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/<int:pk>', CategoriesDetailView.as_view(), name='categories_detail'),
    path('categories/create', CategoriesCreateView.as_view(), name='categories_create'),
    path('categories/<int:pk>/update', CategoriesUpdateView.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete', delete_category, name='categories_delete'),
    path('categories/categories_search/', CategoriesSearchView.as_view(), name='search_view_categories'),
    # session_and_result_urls-------------------------------------------------------------------------------------
    path('program/<int:pk>/session', create_session_and_result, name='session_create'),
    path('session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session/<int:pk>/result', ResultListView.as_view(), name='session_result_view'),
    path('session/result/<int:pk>/update', ResultUpdateView.as_view(), name='session_result_update'),
    # skill urls--------------------------------------------------------------------------------------------------
    path('skill/<int:pk>', SkillDetailView.as_view(), name='skill_detail'),
    path('skill/create', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/update', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/<int:pk>/delete', delete_skill, name='skill_delete'),
    path('skill/skill_search/', SkillSearchView.as_view(), name='search_view_skill')
]
