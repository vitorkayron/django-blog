from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})    

@login_required
def new_post(request):
    if request.method == "GET":
        posts = Post.objects.all()
        authors = User.objects.all()
        return render (request, 'form.html', {'posts': posts,'authors': authors})
    
    elif request.method == "POST":
            title = request.POST.get('title')
            author_id = request.POST.get('author')
            content = request.POST.get('content')
            images = request.FILES.get('images')  # Corrigido: request.FILES em vez de request.POST

            author = get_object_or_404(User, id=author_id)

            post = Post(title=title, content=content, author=author, images=images)
            post.save()
            return redirect('/')
    
    if request.user.is_superuser:
        #allow access only to superuser
        return render(request, 'form.html')
    else:
        #allow access only to user
        return render(request, 'home.html')
    

    
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.views += 1
    post.save()
    return render(request, 'post_detail.html', {'post': post})

def contact(request):
     return render(request, 'contact.html')