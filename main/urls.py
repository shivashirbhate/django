from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classesListing', views.classesListing, name='Classes Listing'),
    path('newStudent', views.newStudentAdd, name='New Student'),
    path('<int:className>/listStudents', views.listStudents, name='List Students'),
    path('<int:studentid>/studentDetails', views.studentDetails, name='Student Details'),
]
