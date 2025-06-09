from django.urls import path
from tasks.views.api import TaskAPI


app_name = "tasks"

api_router = [
    path("tasks", TaskAPI.as_view({"get": "list"}), name="task-list"),
    path("tasks/create", TaskAPI.as_view({"post": "create"}), name="task-create"),
    path("tasks/<int:pk>", TaskAPI.as_view({"get": "retrieve"}), name="task-item"),
    path(
        "tasks/<int:pk>/complete",
        TaskAPI.as_view({"patch": "complete_task"}),
        name="task-complete",
    ),
    path(
        "tasks/<int:pk>/change",
        TaskAPI.as_view({"patch": "partial_update"}),
        name="task-change",
    ),
    path(
        "tasks/<int:pk>/delete",
        TaskAPI.as_view({"delete": "destroy"}),
        name="task-destroy",
    ),
]

web_router = []

urlpatterns = web_router + api_router
