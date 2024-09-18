from django.shortcuts import render
from BlogApp.models import Post

# Create your views here.

def blog(request):
    all_posts = Post.objects.all()   
    return render(request, "BlogApp/blog.html", {"all_posts": all_posts})
