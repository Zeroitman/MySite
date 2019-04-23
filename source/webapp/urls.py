from django.urls import path
from webapp.views import ProgramList, ProgramDetailView, SessionCreateView


app_name = 'webapp'
urlpatterns = [
    path('', ProgramList.as_view(), name='program_list'),
    path('session_create', SessionCreateView.as_view(), name='session_create'),
    # path('current_session/<int:pk>', current_session, name='session_view'), # create separate page
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail')
]




