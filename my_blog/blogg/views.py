from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

from .models import Post

def index(requests):
    late_pubished = Post.title.text()[:5]
    return render(requests, 'home.html', {'late_published' : late_pubished})


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'content', 'keywords', 'description', 'image']


def home(requests):
    return render (requests, 'home.html')

