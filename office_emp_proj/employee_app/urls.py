from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('all_emp/', views.all_emp, name='all_emp'), 
    path('add_emp/', views.add_emp, name='add_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp_no_id'),  # New URL pattern without an emp_id.
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp_with_id'),  # URL pattern with emp_id.
    path('filter_emp/', views.filter_emp, name='filter_emp'),  
    path('filter_emp/<int:emp_id>/', views.filter_emp, name='filter_emp_with_id'),
]
