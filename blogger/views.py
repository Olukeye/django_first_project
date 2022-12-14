from django.shortcuts import render
from .models import Blog


# Create your views here.

def home(request):
    posts = Blog.objects.all()
    return render(request, 'home.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def singleblog(request, pk):
    posts = Blog.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts} )

