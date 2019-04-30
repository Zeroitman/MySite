from django.urls import path
from webapp.views import ProgramDetailView, ProgramListView, \
    SessionDetailView, \
    ChildList, ChildSearchView, ChildListView, ChildDetailView, ChildUpdateView, ChildCreateView, ChildDeleteView, \
    SkillList, SkillDetailView, SkillUpdateView, SkillCreateView, delete_skill, \
    ResultUpdateView, ResultListView, CategoriesListView


# Название приложения, ссылки расставляются в виде webapp:{название шалона}
app_name = 'webapp'

urlpatterns = [
    path('', ChildListView.as_view(), name='child_program_list'),
    path('child/', ChildList.as_view(), name='child_list'),
    path('search/', ChildSearchView.as_view(), name='search_view'),
    path('child/<int:pk>', ChildDetailView.as_view(), name='child_detail'),
    path('child/create', ChildCreateView.as_view(), name='child_create'),
    path('child/<int:pk>/update', ChildUpdateView.as_view(), name='child_update'),
    path('child/<int:pk>/delete', ChildDeleteView.as_view(), name='child_delete'),
    # program urls
    path('program/', ProgramListView.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session_result/<int:pk>', ResultListView.as_view(), name='session_result_view'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    # session urls
    path('session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session/result/<int:pk>', ResultListView.as_view(), name='session_result_view'),
    path('session/result/<int:pk>/update', ResultUpdateView.as_view(), name='session_result_update'),
    # skill urls
    path('skill/', SkillList.as_view(), name='skill_list'),
    path('skill/<int:pk>', SkillDetailView.as_view(), name='skill_detail'),
    path('skill/create', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/update', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/<int:pk>/delete', delete_skill, name='skill_delete'),
]
