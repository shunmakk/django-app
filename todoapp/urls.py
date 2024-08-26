from django.urls  import path
from .views import TaskList, TaskDetail

# 〇〇のURLが来た時、〇〇のviewに関数として渡すパターン分け
urlpatterns = [
    path("", TaskList.as_view()), #ルートディレクトリの場合スラッシュをつけない
    path("task/<int:pk>/", TaskDetail.as_view(), name="task")
]