from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home' ),
    path('add_student/',views.Add_Student, name='add_student'),
    path('delete_student/',views.Delete_Student, name='delete_student'),
    path('edit_student/<int:pk>/',views.editStudent, name='edit_student'),


]