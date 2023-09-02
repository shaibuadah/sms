from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('myAccount/', views.myAccount, name='myAccount'),
    


]

