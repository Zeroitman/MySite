from django.urls import path
from webapp.views import ProgramList, ProgramDetailView, current_session, ProgramListView

app_name = 'webapp'
urlpatterns = [
    path('program/', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('current_session/<int:pk>', current_session, name='session_view'),
    path('list/', ProgramListView.as_view(), name='program_list_view')
]




