from django.urls import path
from webapp.views import ProgramDetailView, SessionCreateView, SessionList, SessionDetailView, ProgramList, ResultList

app_name = 'webapp'


urlpatterns = [
    path('', SessionList.as_view(), name='session_list'),
    path('program/', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('session_create', SessionCreateView.as_view(), name='session_create'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session_result/<int:pk>', ResultList.as_view(), name='session_result_view'),
]




