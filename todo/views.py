from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from todo.models import Tag, Task
from todo.forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    form_class = TaskForm
    template_name = "todo/home.html"
    paginate_by = 5


@require_POST
def toggle_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.status = not task.status
    task.save()
    return redirect('todo:home')


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:home")


class TagListView(ListView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_list.html"
    paginate_by = 5


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tags-list")
