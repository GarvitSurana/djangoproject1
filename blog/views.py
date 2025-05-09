from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Author 1',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date' : '25 march 2025'
    },
    {
        'author' : 'Author 2',
        'title' : 'Blog post 2',
        'content' : 'Second post content',
        'date' : '25 march 2025'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request , 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
