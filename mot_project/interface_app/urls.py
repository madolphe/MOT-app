from django.urls import path, re_path
from . import views
from django.utils import timezone
import datetime


urlpatterns = [
    path('', views.login_page, name='login_page'),
    re_path(r'^study=(.*)$', views.login_page, name='login_page'), # Still not sure how this works, but it prevents the login page warning if user logs out from interface
    path('home', views.home, name='home'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('signup_page', views.signup_page, name='signup_page'),
    path('consent_page', views.consent_page, name='consent_page'),
    path('off_session_page', views.off_session_page, name='off_session_page'),
    path('start_task', views.start_task, name='start_task'),
    path('end_task', views.end_task, name='end_task'),
    path('end_session', views.end_session, name='end_session'),
    path('thanks_page', views.thanks_page, name='thanks_page'),
    path('app_2D', views.visual_2d_task, name='app_2D'),
    path('app_3D', views.visual_3d_task, name='app_3D'),
    path('app_MOT', views.MOT_task, name='app_MOT'),
    path('next_episode', views.next_episode, name='next_episode'),
    path('restart_episode', views.restart_episode, name='restart_episode'),

    ## JOLD urls
    path('JOLD/practice-LL', views.jold_start_ll_practice, name='jold_start_ll_practice'),
    path('JOLD/save-trial', views.jold_save_ll_trial, name='jold_save_ll_trial'),
    path('JOLD/close-LL-practice', views.jold_close_ll_practice, name='jold_close_ll_practice'),
    path('JOLD/QuestionBlock/', views.joldQuestionBlock, name='JOLD_question_block'),
    path('JOLD/close-session', views.jold_free_choice, name='jold_free_choice'),
    path('JOLD/close-session/<int:choice>/', views.jold_free_choice, name='jold_free_choice')
]
