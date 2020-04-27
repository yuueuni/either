from django.urls import path
from . import views

app_name = 'votes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:vote_pk>/detail/', views.detail, name='detail'),
    path('<int:vote_pk>/comment/', views.comment, name='comment'),
    path('<int:vote_pk>/<int:comment_pk>/delete_comment/', views.delete_comment, name='delete_comment'),
]