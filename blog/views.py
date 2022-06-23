from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

from .models import Post

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('blog:all')

class PostDeleteView(generic.ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('blog:all')

class PostUpdateView(generic.ListView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy('blog:all')

class PostDetailView(generic.DetailView):
    model = Post
