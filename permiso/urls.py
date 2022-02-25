from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name="login"),
    path('student',views.student,name="student"),
    path('personnel',views.personnel,name="personnel"),
    path('gmail',views.gmail,name="gmail"),
    path('notify',views.notify,name="notify"),
    path('middle',views.middle,name="middle"),
    path('fun',views.fun,name='fun'),
    path('dash',views.dash,name="dash"),
    path('approved',views.approved,name="approved"),
]