from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import Post

# Create your views here.
#ListView은 데이터를 전체를 보여주는 기능
class PostList(ListView):
    model =Post
    #mplate_name = 'blog/post_list.html'
    ordering = '-pk'

#DetailView은 데이터를 하나만 불러서 보여주는 기능
class PostDetail(DetailView):
    model =Post
    #template_name = 'blog/post_detail.html' 클래스 이름 생략 가능
    ordering = '-pk'