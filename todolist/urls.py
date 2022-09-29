from todolist.views import *
from django.urls import path

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path("new-task/", new_task, name="new_task"),
    path("is_finished_status/<int:id_task>", is_finished_status, name="is_finished_status"),
    path("remove/<int:id_task>", remove, name="remove"),
]