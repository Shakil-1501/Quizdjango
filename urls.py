# Core Django imports.
from django.urls import path
from django.shortcuts import redirect, render

# LMS app imports

from lms.views.course.course_views import (
    CourseListView,fetch_questions,compute_stats,display_lp,Edit_quiz,preview_quiz,fetch_questions_oneatatime,compute_html,enter_comment,quiz_lp
)



from lms.views.dashboard.student.dashboard_views import (
    DashboardHomeView,
)

from lms.views.account.register_view import \
    (
      ActivateView,
      AccountActivationSentView,
      UserRegisterView,
    )

from lms.views.account.logout_view import UserLogoutView
from lms.views.account.login_view import UserLoginView

# Specifies the app name for name spacing.
app_name = "lms"

# lms/urls.py
urlpatterns = [

    # LMS URLS #

    # /home/
    path(
        route='',
        view=CourseListView.as_view(),
        name='home'
    ),
    path('lms/course',compute_stats,name="compute_stats"),
    
    
   
    path('lms/quiz',fetch_questions_oneatatime,name="fetch_questions_oneatatime"),

    path('lms/quiz3',fetch_questions,name="fetch_questions"),

    path('lms/quizlp',quiz_lp,name="quiz_lp"),

    path('lms/quiz2',display_lp,name="display_lp"),

    path('admin/',Edit_quiz,name="Edit_quiz"),

    path('lms/quizs',preview_quiz,name="preview_quiz"),

    path('lms/file',compute_html,name="compute_html"),

    path('lms/enter_comment',enter_comment,name="enter_comment"),

    #path('quiz2', lambda request: render(request, 'templates/lms/quiz2.html')),
  
    

    
    
    # ACCOUNT URLS #

    # /account/login/
    path(
        route='account/login/',
        view=UserLoginView.as_view(),
        name='login'
    ),

    # /account/login/
    path(
        route='account/register/',
        view=UserRegisterView.as_view(),
        name='register'
    ),

    # /account/logout/
    path(
        route='account/logout/',
        view=UserLogoutView.as_view(),
        name='logout'
    ),

    path(route='account_activation_sent/',
         view=AccountActivationSentView.as_view(),
         name='account_activation_sent'
         ),

    path(route='activate/<uidb64>/<token>/',
         view=ActivateView.as_view(),
         name='activate'
         ),

    # DASHBOARD URLS #

    # /author/dashboard/home/
    path(
        route="student/dashboard/home/",
        view=DashboardHomeView.as_view(),
        name="dashboard_home"
    ),

]

