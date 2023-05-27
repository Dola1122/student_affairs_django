from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('html/login.html',views.login_view,name='login_view'),
    path('html/signup.html',views.signup,name='signup'),
    path('html/home.html',views.home,name='home'),
    path('html/add_student.html',views.add_student,name='add_student'),
    path('html/search.html',views.search,name='search'),
    path('html/student_list.html',views.student_list,name='student_list'),
    #path('html/edit_student.html',views.edit_student,name='edit_student'),
    #path('html/assign_department.html',views.assign_department,name='assign_department'),
    path('html/edit_student.html/<int:id>',views.edit_student,name='edit_student'),
    path('html/edit_student.html/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),         
    path('delete/<int:id>', views.delete, name='delete'),
]