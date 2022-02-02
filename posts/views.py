from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.filter()
    context = {'posts': posts}
    template_name = 'posts/index.html'
    return render(request, template_name, context)
