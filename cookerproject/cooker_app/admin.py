from django.contrib import admin

# Register your models here.

from .models import Article
from .models import Category
from .models import Comment

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["content", "article_id", "path","author_id" ,"pub_date" ]

admin.site.register(Comment, CommentModelAdmin)    

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    list_display_links = ["name"]

admin.site.register(Category,CategoryModelAdmin)    

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Article

admin.site.register(Article, ArticleModelAdmin)

