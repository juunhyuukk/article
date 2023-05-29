from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:pk>', views.detail, name = 'detail'),
    # path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    # 데이터 삭제에 대한 URL 패턴
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    # 데이터 수정 페이지에 대한 URL 패턴
    # path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
]
