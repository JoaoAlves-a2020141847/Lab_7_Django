from django.urls import path
from . import views

#URLs para as diferentes páginas
urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('topic/<int:topic_id>/add_comment', views.add_comment, name='add_comment'),
    path('topic/<int:topic_id>/edit_topic', views.edit_topic, name='edit_topic'),
    path('topic/<int:topic_id>/delete_topic', views.delete_topic, name='delete_topic'),
    path('new_topic', views.new_topic, name='new_topic')
]