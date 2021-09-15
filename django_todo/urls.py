"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.output_todo_list, name="todo_list"),
    path('add_item_manual', views.create_todo_item_manual, name="add_item_manual"),
    path('add_item_auto', views.create_todo_item_auto, name="add_item_auto"),
    path('edit_item_auto/<item_id>', views.update_todo_item_auto, name="edit_item_auto"),
    path('toggle_done/<item_id>', views.toggle_todo_done, name="toggle_done"),
]
