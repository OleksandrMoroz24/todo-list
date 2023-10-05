from django.urls import path

from todo.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)


urlpatterns = [
    path("", TaskListView.as_view, name="home"),
    path("task/add/", TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path("tags/", TagListView.as_view, name="tags-list"),
    path("tags/add/", TagCreateView.as_view(), name='tags-add'),
    path('tags/<int:pk>/edit/', TagUpdateView.as_view(), name='tags-edit'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tags-delete'),

]

app_name = "todo"
