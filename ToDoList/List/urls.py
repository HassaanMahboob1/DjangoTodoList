from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_view, name="create_view"),
    path("viewlist", views.view_list, name="view_list"),
    path("viewlist/deletelist/<list_id>", views.delete_item, name="delete_item"),
    path("viewlist/editlist/<list_id>", views.edit_item, name="edit_item"),
    path("edited/<list_id>", views.edited, name="edited"),
]
