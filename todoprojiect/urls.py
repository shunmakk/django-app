# urls.py
from django.contrib import admin
from django.urls import path, include  # Django の include をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    # todoappディレクトリ内のurls.pyで実行するという宣言
    path("", include("todoapp.urls")),
]
