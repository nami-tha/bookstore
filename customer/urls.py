from customer import  views
from django.urls import path
urlpatterns=[
    path("home",views.CustomerHome.as_view(),name="home"),
    path("signup", views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="login"),
    path("signout", views.sign_out, name="signout"),

]