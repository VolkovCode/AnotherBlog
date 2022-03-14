from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import (Follow, 
                    Like, 
                    Post, 
                    Categories, 
                    User, 
                    Comment
                    )
from .forms import CommentForm, PostForm

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}         
    template_name = 'posts/index.html'
    return render(request, template_name, context)


def post(request, id, slug):
    post = get_object_or_404(Post, pk=id)
    template = 'posts/post.html'
    form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    context = {
        'post': post,
        'comments': comments,
        'form': form,
        }
    return render(request, template, context)

@login_required
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

def profile(request, username):
    author = get_object_or_404(User, username=username)  
    posts = Post.objects.filter(author=author)
    follow = Follow.objects.filter(follower=request.user, following=author)
    context = {
        'posts': posts,
        'follow': follow,
        'author': author,
    }
    template = 'posts/profile.html'
    return render(request, template, context)

@login_required
def add_comment(request, slug, id):
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post', slug=post.slug, id=id)
        return render(request, "posts/post.html", {'form': form, 'post':post})    
    form = CommentForm()
    return render(request, "posts/comment.html", {"post": post, "form": form, 'comments': comments})

@login_required
def delete_comment(request, slug, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(pk=comment_id)
    comment.delete()
    if request.user.username != comment.author.username:
        return redirect('post', slug=post.slug, id=post.id)        
    return redirect('post', slug=post.slug, id=post.id)

@login_required
def follow(request, username):
    author = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(follower=request.user, following=author)
    print(follow)
    if not follow:
        Follow.objects.create(follower=request.user, following=author)
        print(follow)
        return redirect('profile', username)
    else:
        return redirect('profile', username)    

@login_required
def unfollow(request, username):
    author = get_object_or_404(User, username=username)
    follow = Follow.objects.filter(follower=request.user, following=author)
    if follow:
        follow.delete()
        return redirect('profile', username)
    else:
        return redirect('profile', username) 

def like(request, slug, id):
    #user = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=id)
    like = Like.objects.filter(liker = request.user, post = post)
    if not like:
        Like.objects.create(liker = request.user, post = post)
        print(like)
        return redirect('post', slug, id)
    else:
        return redirect('post', slug, id)
        
