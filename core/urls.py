from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.dashboard,name='dashboard'),
    path('all_tasks/',views.display,name='display'),
    path('task/<int:task_id>/update/', views.update_status, name='update_status'),

]