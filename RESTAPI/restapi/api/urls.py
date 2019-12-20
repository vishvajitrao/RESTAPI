from django.urls import path,include
from . import views
from api.views import StudentList,Studentlist,Student_list,Student_detail
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('',views.Index,name='Index'),

    #function based views
    path('students/',views.student_list),
    path('students/<int:pk>/',views.student),
    path('login/',obtain_auth_token,name='login'),

    #classed based views
    path('allstudents/',Student_list.as_view(),name = 'allstudent'),
    path('allstudent/<int:pk>/',Student_detail.as_view(),name = 'allstudent'),
    


    #create api using mixins
    path('studentlist',StudentList.as_view()),
    path('studentlist/<int:id>/',Studentlist.as_view()),

    #authenticate and permission
     path('api-auth/', include('rest_framework.urls')),
]