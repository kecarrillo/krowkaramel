from django.shortcuts import render, get_object_or_404
from .models import Post, CategoryPost

def blog_category(request, category):
    cat= get_object_or_404(CategoryPost, name=category)
    posts = Post.objects.filter(category_blog=cat)
    return render(request, 'blog/post_list.html', {'category': cat, 'posts': posts})

def menu(request):
    category = CategoryPost.objects.all()
    return render(request, 'blog/menu.html', {'category': category})