from django.urls import path
from webapp.views import ProgramDetailView, SessionCreateView, SessionList, SessionDetailView


app_name = 'webapp'


urlpatterns = [
    path('', SessionList.as_view(), name='session_list'),
    path('session_create', SessionCreateView.as_view(), name='session_create'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail')
]




