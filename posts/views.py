from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post, Categories

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    cat = []
    for post in posts:
        for c in post.category.all():
            cat.append(c.slug)
    print(cat)           
    template_name = 'posts/index.html'
    return render(request, template_name, context)


def post(request, id, slug):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}
    template = 'posts/post.html'
    return render(request, template, context)

