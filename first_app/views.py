from first_app.models import TaskModel
from first_app.forms import TaskStoreForm 
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class TaskFormView(CreateView):
    model = TaskModel
    template_name = 'add_task.html'
    form_class = TaskStoreForm
    success_url = reverse_lazy('show_tasks')

class TaskListView(ListView):
    model = TaskModel
    template_name = 'home.html'
    context_object_name = 'tasklist'

class TaskUpdateView(UpdateView):
    model = TaskModel
    form_class = TaskStoreForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('show_tasks')    

class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    success_url = reverse_lazy('show_tasks')

class CompleteView(DeleteView):
    model = TaskModel
    template_name = 'complete_confirm.html'
    success_url = reverse_lazy('show_tasks')
    
    