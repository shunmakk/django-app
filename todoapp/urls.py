from django.urls  import path
from .views import TaskList, TaskDetail,TaskCreate

# 〇〇のURLが来た時、〇〇のviewに関数として渡すパターン分け
urlpatterns = [
    path("", TaskList.as_view(),name="tasks"), #ルートディレクトリの場合スラッシュをつけない
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task", TaskCreate.as_view(), name="create-task")
]