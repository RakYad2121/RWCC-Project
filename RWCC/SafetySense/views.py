from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

class PostBlog(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_blog.html"
    success_url = reverse_lazy('home')

class UpdateBlog(UpdateView):
    model = Post
    template_name = 'update_blog.html'
    fields = ['title', 'body']

class DeleteBlog(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

