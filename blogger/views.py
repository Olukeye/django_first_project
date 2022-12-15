from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog



def home(request):
    posts = Blog.objects.all()
    return render(request, 'home.html', {'posts': posts})


# this class function is for list of post which inherit from Blog model
class PostListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Blog


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# def singleblog(request, pk):
#     posts = Blog.objects.get(id=pk)
#     return render(request, 'posts.html', {'posts': posts} )

