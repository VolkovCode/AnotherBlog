from django.urls import path
from .views import index, new_post, post

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>-<slug:slug>/', post, name='post'),
    path('new-post/', new_post, name='new-post')
]