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

##paginate_by는 한 페이지당 몇개 데이터를 보여줄꺼다라는 의미
class PostList(ListView):
    model = Post
    # template_name = 'blog/post_list.html'
    paginate_by = 2   # pagination 기능 활성화, page 당 3개 
    ordering = '-pk'