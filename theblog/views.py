from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request, 'home.html',{})

class TutorialHome(ListView):
    model = Post
    template_name = 'tutorialhome.html'
    # ordering = ['-id']

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    # ordering = ['-post_date']

     
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    # fields = ['title','title_tag','body'] 

class DeletePostView(DeleteView):
    model = Post
    # form_class = EditForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

