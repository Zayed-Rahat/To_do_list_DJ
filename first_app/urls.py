from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='show_tasks'),
    path('add_new_task/', views.TaskFormView.as_view(), name='add_task'),
    # path('all_tasks/', views.TaskListView.as_view(), name='show_tasks'),
    path('edit_task/<int:pk>', views.TaskUpdateView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', views.DeleteTaskView.as_view(), name='delete_task'),
    path('complete_confirm/<int:pk>', views.CompleteView.as_view(), name='complete_confirm'),

]
