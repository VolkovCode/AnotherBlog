from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .models import Post, Categories
from .forms import PostForm

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

def new_post(request):
    user = request.user
    form = PostForm(request.POST or None, files=request.FILES or None)
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        if form.is_valid():
            n_post = form.save(commit=False)
            n_post.author = user
            n_post.save()
            return redirect('index')
        return render(request, 'posts/new_post.html', {'form': form})        
    form = PostForm()
    return render(request, 'posts/new_post.html', {'form': form}) 
