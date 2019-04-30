from django.urls import path
from webapp.views import ProgramDetailView, ChildProgramList, SessionDetailView, ProgramList, ResultList, ChildList, ChildSearchView

app_name = 'webapp'


urlpatterns = [
    path('', ChildProgramList.as_view(), name='child_program_list'),
    path('program/', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('child/', ChildList.as_view(), name='child_list'),
    path('search/', ChildSearchView.as_view(), name='search_view'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session_result/<int:pk>', ResultList.as_view(), name='session_result_view'),
]




