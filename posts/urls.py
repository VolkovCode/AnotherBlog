from django.urls import path
from .views import (
    index, 
    new_post, 
    post, 
    profile, 
    add_comment,
    delete_comment
)

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>-<slug:slug>/', post, name='post'),
    path('new-post/', new_post, name='new-post'),
    path('<str:username>', profile, name = 'profile'),
    path("<int:id>-<slug:slug>/comment/", add_comment, name="add_comment"), 
    path("<int:post_id>-<slug:slug>/comment/<int:comment_id>/delete", delete_comment, name="delete_comment"),
]