from django.urls  import path
from .views import TaskList, TaskDetail,TaskCreate, TaskUpdate,TaskDelete

# 〇〇のURLが来た時、〇〇のviewに関数として渡すパターン分け
urlpatterns = [
    path("", TaskList.as_view(),name="tasks"), #ルートディレクトリの場合スラッシュをつけない
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
]