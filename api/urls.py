from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<str:pk>', views.task_detail, name="task-detail"),
    path('task-create/', views.task_create, name="task-create"),
    path('task-update/<str:pk>', views.task_update, name="task-update"),
    path('task-delete/<str:pk>', views.task_delete, name="task-delete"),

    path('login/', views.login, name="login"),

    path('outward-list/', views.outward_list, name="outward-list"),
    path('outward-detail/<str:pk>', views.outward_detail, name="outward-detail"),
    path('outward-create/', views.outward_create, name="outward-create"),
    path('outward-update/<str:pk>', views.outward_update, name="outward-update"),
    path('outward-delete/<str:pk>', views.outward_delete, name="outward-delete"),

    path('inward-list/', views.inward_list, name="inward-list"),
    path('inward-detail/<str:pk>', views.inward_detail, name="inward-detail"),
    path('inward-create/', views.inward_create, name="inward-create"),
    path('inward-update/<str:pk>', views.inward_update, name="inward-update"),
    path('inward-delete/<str:pk>', views.inward_delete, name="inward-delete"),
]
