from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home),
    path('roadmaps/',views.roadmaps),
    path('study-planner/',views.study_planner),
    path('interview-questions/',views.interview_questions),
    path('resources/',views.resources),
    path('predict-career/',views.predict_career),
    path('analyze-resume/',views.analyze_resume),
    path('start-assessment/',views.start_assessment),
    path('signup/',views.signup_view),
    path('login/',views.login_view),
    path('logout/',views.logout_view),
]