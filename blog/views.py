from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model =Post
    #mplate_name = 'blog/post_list.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model =Post
    #template_name = 'blog/post_detail.html' 클래스 이름 생략 가능
    ordering = '-pk'