from django.urls import path
from webapp.views import ProgramDetailView, SessionDetailView, ProgramListView, ResultListView, \
    ChildListView, ChildDetailView, ChildUpdateView, ChildCreateView, ChildDeleteView, \
    ResultUpdateView

app_name = 'webapp'

urlpatterns = [
    path('', ChildListView.as_view(), name='child_list'),
    path('child_profile/<int:pk>', ChildDetailView.as_view(), name='child_detail'),
    path('child/<int:pk>/update', ChildUpdateView.as_view(), name='child_update'),
    path('child/create', ChildCreateView.as_view(), name='child_create'),
    path('child/<int:pk>/delete', ChildDeleteView.as_view(), name='child_delete'),
    path('program/', ProgramListView.as_view(), name='program_list'),
    path('program/<int:pk>', ProgramDetailView.as_view(), name='program_detail'),
    path('current_session/<int:pk>', SessionDetailView.as_view(), name='session_view'),
    path('session_result/<int:pk>', ResultListView.as_view(), name='session_result_view'),
    path('session_result/<int:pk>/update', ResultUpdateView.as_view(), name='session_result_update'),
]
