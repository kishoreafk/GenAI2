from django.urls import path
from .views import register, user_login, user_logout, dashboard, admin_dashboard, judge_dashboard, participant_dashboard

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('admin-dashboard/', admin_dashboard, name="admin_dashboard"),
    path('judge-dashboard/', judge_dashboard, name="judge_dashboard"),
    path('participant-dashboard/', participant_dashboard, name="participant_dashboard"),
]
