from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.myAccount),
    path('Schoolregistration/', views.Schoolregistration, name='Schoolregistration'),

    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('adminProfile/', views.adminProfile, name='adminProfile'),

    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('schoolDashboard/', views.schoolDashboard, name='schoolDashboard'),
    path('deptDashboard/', views.deptDashboard, name='deptDashboard'),

    path('school/', include('school.urls')),
]