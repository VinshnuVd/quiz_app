from django.urls import path
from users.views import register,Login


urlpatterns=[
    path("register/",register,name="userregister"),
    path("login/",Login.as_view(),name="userlogin"),
]