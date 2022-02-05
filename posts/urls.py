from django.urls import path
from .views import index, post

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>-<slug:slug>/', post, name='post')
]