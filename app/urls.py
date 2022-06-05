from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtask/',views.AddTask,name='AddTask'),
    path('adding',views.AddedTask,name='addedtask'),
    path('updatetask/<int:id>',views.Getupdate,name='getupdate'),
    path('updating/<int:id>',views.Updating,name='Updating'),
    path('deletetask/<int:id>',views.deleteTask,name='delete')
]