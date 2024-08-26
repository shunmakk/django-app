from django.urls  import path
from .views import TaskList

# 〇〇のURLが来た時、〇〇のviewに関数として渡すパターン分け
urlpatterns = [
    path("", TaskList.as_view()) #ルートディレクトリの場合スラッシュをつけない
]