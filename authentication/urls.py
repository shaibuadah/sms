from django.urls import path, include
from . import views
from school.views import schoolDashboard


urlpatterns = [
    # path('', views.myAccount),
    path('Schoolregistration/', views.Schoolregistration, name='Schoolregistration'),

    path('authentication/login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('adminProfile/', views.adminProfile, name='adminProfile'),

    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('schoolDashboard/', schoolDashboard, name='schoolDashboard'),
    path('deptDashboard/', views.deptDashboard, name='deptDashboard'),

    path('school/', include('school.urls')),
]