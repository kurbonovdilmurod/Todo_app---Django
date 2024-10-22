from django.urls import path
from todo import views

urlpatterns = [
    path('', views.add_todo, name='add_todo'),
    path('<int:pk>/', views.view_todo, name='view_todo'),
    path('edit/<pk>', views.edit_todo, name='edit_todo'),
    path('delete/<pk>', views.delete_todo, name="delete_todo"),
    path('cross_off/<pk>', views.cross_off_todo, name="cross_off_todo"),
    path('uncross/<pk>', views.uncross_todo, name="uncross_todo"),

]