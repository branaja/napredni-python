from django.urls import path

from tasks import views

urlpatterns = [

    #path('', views.IndexView.as_view(), name='index'),
    #path('index', views.IndexView.as_view(), name='index'),
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:task_id>/', views.TaskDetailsView.as_view(), name='details'),
    path('<int:task_id>/edit/', views.TaskEditView.as_view(), name='edit'),
    path('<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('add/', views.TaskAddView.as_view(), name='add'),
]