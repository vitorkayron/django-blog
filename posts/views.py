from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post(request):
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



