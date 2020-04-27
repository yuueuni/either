from django.urls import path
from . import views

app_name = 'votes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:vote_pk>/detail/', views.detail, name='detail'),
    path('<int:vote_pk>/update/', views.update, name='update'),
    path('<int:vote_pk>/delete_vote/', views.delete_vote, name='delete_vote'),
    path('<int:vote_pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:vote_pk>/<int:comment_pk>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('random/', views.random, name='random'),
]