from django.urls import path
from webapp.views import ProgramList, SessionDetail


app_name = 'webapp'
urlpatterns = [
    path('', ProgramList.as_view(), name='program_list'),
    path('session/<int:pk>', SessionDetail.as_view(), name='session_view')
]




