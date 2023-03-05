from django.urls import path
from . import views

app_name = "doctor"   


urlpatterns=[
       path("register_doctor", views.register_doctor, name="register_doctor"),
        path("listby_spec", views.listby_spec, name="listby_spec"),
         path("findby_spec", views.findby_spec, name="findby_spec"),
       path("doctor_list",views.doc_list,name="doctor_list"),
          path("register_request_doctor",views.register_request_doctor,name="registered_doctor"),
]