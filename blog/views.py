from django.shortcuts import render ,redirect
from django.views.generic import ListView ,DetailView, CreateView, UpdateView
from .models import Post, Category, Tag
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .form import PostForm
from django.utils.text import slugify

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

#포스트 새로 생성하는 코드
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def form_valid(self, form):
        current_user = self.request.user        
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):            
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            self.object.tags.clear()           
            tags_str = self.request.POST.get('tags_str')
            
            if tags_str : 
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',',';')
                tags_list = tags_str.split(';')

                for t in tags_list : 
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name = t)
                    if is_tag_created :
                        tag.slug = slugify(t, allow_unicode =True) #allow_unicode는 한글허용
                        tag.save()
                    self.object.tags.add(tag)
                return response
            else :
                return redirect('/blog/')

#포스트 수정하는 코드
class PostUpdate(LoginRequiredMixin ,UpdateView):
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category','tags']

    template_name = 'blog/post_update_form.html'

#작성자만 수정할 수있게 해주는 코드
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate,self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, **kwargs):
        context = super(PostUpdate,self).get_context_data()
        if self.object.tags.exisits():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = ';'.join(tags_str_list)
        return context

def category_page(request, slug):

    if slug == 'no_category':
        category = '미분류'
        post_list= Post.objects.filter(category=None)
    else:
        category= Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)


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


