from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.user_login, name='login'),
   path('first', views.first,name='first'),
   path('trainings', views.trainings, name="trainings"),
   path('jobs', views.jobs,name='jobs'),
   path('profile', views.profile, name='profile'),
   path('signup/', views.signup, name='signup'),
   path('logout/', views.user_logout, name='logout'),
   path('worker_dashboard', views.worker_dashboard, name='worker_dashboard'),
   

]
