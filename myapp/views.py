from django.http import HttpResponse, JsonResponse
from .models import Project, Task
# El render es para que se puedan enviaar páginas completas y no un solo string.
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = "Django Course!!"
    return render(request, "index.html", {
        # El primer title se puede llamar como sea, el segundo hace referencia a la variable que cree antes.
        "title": title
    })


# El request se coloca aquí, más que nada por regla. Ya que, de lo contrario da error.
def hello(request, username):
    # Esto lo que hace es poner la variable de username en el %s
    return HttpResponse("<h2>Hello %s</h2>" % username)


def about(request):
    username = "Luis"
    return render(request, "about.html", {
        "username": username
        # Siempre se debe poner el "request, ", ya que de lo contrario no funciona.
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {
        "projects": projects
    })


def tasks(request):
    # task = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, "tasks/tasks.html", {
        "tasks": tasks
    })


def create_task(request):
    if request.method == "GET":
        return render(request, "tasks/create_task.html", {
            "form": CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST["title"],
                            description=request.POST["description"], project_id=2)
        return redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(request, "projects/create_project.html", {
            "form": CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect("projects")
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id) # se pone el project_id porque así aparece en el SQL
    return render(request, "projects/detail.html", {
        "project": project,
        "tasks": tasks
    })
