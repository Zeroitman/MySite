from django.urls import path
from webapp.views import ProgramList, ProgramDetailView


app_name = 'webapp'
urlpatterns = [
    path('', ProgramList.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail')
]




