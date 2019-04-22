from django.urls import path
from webapp.views import ProgramList, ProgramDetailView, current_session


app_name = 'webapp'
urlpatterns = [
    path('', ProgramList.as_view(), name='program_list'),
    path('current_session/<int:pk>', current_session, name='session_view'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail')
]




