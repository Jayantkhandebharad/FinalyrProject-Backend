from django.urls import path
from . import views

app_name = "main"   


urlpatterns = [
    path("register", views.register, name="register"),
   path("register_request",views.register_request,name="registered"),
      path("login_page",views.login_page,name="login_page"),
   path("login_request", views.login_request, name="login")
    # path("register", views.register_request, name="register")
]