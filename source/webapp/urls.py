from django.urls import path
from webapp.views import ProgramList


app_name = 'webapp'
urlpatterns = [
    path('', ProgramList.as_view(), name='program_list')
]




