from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView )
from .models import Blog



def home(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, 'blogger/home.html', context)


# this class function is for list of post which inherit from Blog model
class BlogListView(ListView):
    model = Blog
    template_name = 'blogger/home.html'
    context_object_name = 'posts'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blogger/about.html')


def contact(request):
    return render(request, 'blogger/contact.html')


# def singleblog(request, pk):
#     posts = Blog.objects.get(id=pk)
#     return render(request, 'posts.html', {'posts': posts} )

