from django.urls import path

from . import views

urlpatterns = [
    path('', views.Homepage, name = ""),
    
    path('login', views.login, name="login"),
    path('addbook', views.Addbook, name="Addbook"),
    path('register', views.CreateUser, name="register"),
    path('View_Books', views.View_Books, name="ViewBooks"),
    path('Borrow', views.Check_out, name="Borrow"),
    path('Transactions', views.Trans_Hist, name="Transactions"),
]