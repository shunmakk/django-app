from django.urls  import path
from . import views

# 〇〇のURLが来た時、〇〇のviewに関数として渡すパターン分け
urlpatterns = [
    path("", views.taskList) #ルートディレクトリの場合スラッシュをつけない
]