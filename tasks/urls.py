from django.urls import path

from tasks.views import about_website, create_task, home_page, list_tasks, read_task, delete_task, update_task


urlpatterns = [
    path('', home_page, name='home-page'), 
    path('tasks/create/', create_task, name='create-task'),
    path('tasks/list/', list_tasks, name='list-tasks'),
    path('task/<int:task_id>/', read_task, name='read-task'), 
    path('task/<int:task_id>/delete/', delete_task, name='delete-task'),
    path('task/<int:task_id>/update/', update_task, name='update-task'),
    path('task/about', about_website, name='about-website'),
]
