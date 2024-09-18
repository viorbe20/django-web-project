from django.shortcuts import render
from BlogApp.models import Post, Category

# Create your views here.

def blog(request):
    all_posts = Post.objects.all()   
    return render(request, "BlogApp/blog.html", {"all_posts": all_posts})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts_per_category = Post.objects.filter(categories=category)
    all_posts = Post.objects.all()  
    return render(request, "BlogApp/categories.html", {"category": category, "posts_per_category": posts_per_category, "all_posts": all_posts})