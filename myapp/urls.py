from django.urls import path
from . import views  # El punto se utiliza para indicar que se esta importando de esta misma carpeta.

urlpatterns = [
    path('', views.index, name="index"),
    path("about/", views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello" ),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:id>", views.project_detail, name="project_detail"),
    path("tasks/", views.tasks, name="tasks"),
    path("create_task/", views.create_task, name="create_task"),
    path("create_project", views.create_project, name="create_project"),
]
# Se coloca el name para que se pueda hacer referencia a estas URL por medio de su nombre y no por el URL en sí.