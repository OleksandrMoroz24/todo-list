from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy

from todo.models import Tag, Task
from todo.forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    form = TaskForm
    template_name = "todo/home.html"
    paginate_by = 5


class TaskCreateView(CreateView):
    model = Task
    form = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(UpdateView):
    model = Task
    form = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:home")


class TagListView(ListView):
    model = Tag
    form = TagForm
    template_name = "todo/tag_list.html"
    paginate_by = 5


class TagCreateView(CreateView):
    model = Tag
    form = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")


class TagUpdateView(UpdateView):
    model = Tag
    form = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag_list")

