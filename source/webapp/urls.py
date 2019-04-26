from django.urls import path
from webapp.views import ProgramDetailView, ChildList, SessionDetailView, ProgramList, ResultList

app_name = 'webapp'


urlpatterns = [
    path('', ChildList.as_view(), name='child_list'),
    path('program/', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session_result/<int:pk>', ResultList.as_view(), name='session_result_view'),
]




