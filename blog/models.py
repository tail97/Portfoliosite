from django.db import models
from django.contrib.auth.models import User
import os


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique= True)
    slug = models.SlugField(max_length=200, unique= True, allow_unicode= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    class Meta:
        # 폴더명 다시 설정
        verbose_name_plural = "Categories"



class Tag(models.Model):
    name = models.CharField(max_length=50, unique= True)
    slug = models.SlugField(max_length=200, unique= True, allow_unicode= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'



class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #add 할 때의 시간
    updated_at = models.DateTimeField(auto_now=True) #update 할 때의 시간
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank = True)
    file_upload = models.FileField(upload_to = 'blog/file/%Y/%m/%d/',blank = True )
    hook_text = models.CharField(max_length=100, blank=True)
    
    # author = models.ForeignKey(User,on_delete = models.CASCADE) # 포스트의 작성자가 데이터베이스에서 삭제되었을때 이포스트도 같이 삭제한다
    # 포스트의 작성자가 데이터베이스에서 삭제되었을때 포스트도 같이 삭제한다
    author = models.ForeignKey(User, null= True, on_delete = models.SET_NULL)
    category = models.ForeignKey(Category,null= True,blank=True, on_delete= models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    


    def __str__(self):

        return f'[{self.pk}]--{self.title} ::{self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]



