from django.shortcuts import render
from django.views.generic import ListView ,DetailView, CreateView
from .models import Post, Category, Tag

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

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

##paginate_by는 한 페이지당 몇개 데이터를 보여줄꺼다라는 의미
class PostList(ListView):
    model = Post
    # template_name = 'blog/post_list.html'
    paginate_by = 2   # pagination 기능 활성화, page 당 3개 
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category']

def category_page(request, slug):

    if slug == 'no_category':
        category = '미분류'
        post_list= Post.objects.filter(category=None)
    else:
        category= Category.objects.get(slug=slug)
        Post_list = Post.objects.filter(category=category)


    return render(
        request,
        'blog/post_list.html',
        {'post_list': post_list,
         'categories': Category.objects.all(),
         'no_category_post_count': Post.objects.filter(category=None).count(),
         'category': category,
        }
    )



def tag_page(request, slug):
    tag= Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()


    return render(
        request,
        'blog/post_list.html',
        {'post_list': post_list,
         'tag': tag,
         'categories': Category.objects.all(),
         'no_category_post_count': Post.objects.filter(category=None).count(),
        }
    )

