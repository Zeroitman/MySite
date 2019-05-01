from django.urls import path
from webapp.views import ProgramDetailView, SessionList, \
    SessionDetailView, ProgramList, ResultList, counter_done, counter_done_with_hint

app_name = 'webapp'


urlpatterns = [
    path('', SessionList.as_view(), name='session_list'),
    # counter urls
    path('skill_w_hint/<int:pk>', counter_done_with_hint, name='done_w_hint'),
    path('skill_done/<int:pk>', counter_done, name='counter_done'),
    # programs
    path('program', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    # session with session results
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_detail'),
    path('session_result', ResultList.as_view(), name='session_result_view'),
]




