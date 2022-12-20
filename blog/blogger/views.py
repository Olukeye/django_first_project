from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,  DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Blog
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
def about(request):
    return render(request, 'blogger/about.html')


def contact(request):
    return render(request, 'blogger/contact.html')


# def singleblog(request, pk):
#     posts = Blog.objects.get(id=pk)
#     return render(request, 'posts.html', {'posts': posts} )

