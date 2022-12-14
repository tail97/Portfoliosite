from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    # category모델의 name 필드에 값이 입력됐을 때 자동으로 slug가 만들어진다 .
    prepopulated_fields = {'slug':('name',) }

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)
