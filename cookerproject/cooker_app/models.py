from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Кагория')
    slug = models.SlugField(verbose_name='Транслит', null=True)    

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" %(self.id)    

	
class Article(models.Model):
    title =  models.CharField(max_length = 120)
    description = models.TextField(default='Description')
    keywords = models.CharField(max_length = 120, default='Key words')
    image = models.FileField(null=True, blank=True)
    content = RichTextUploadingField()
    visible = models.BooleanField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='categories')

    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" %(self.id)

    class Meta:
        ordering = ["-id", "-timestamp"]
    
class Comment(models.Model):
    class Meta:
        db_table = "comments"

    path = ArrayField(models.ImageField())
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

    def __str__(self):
        return self.content[0:200]

    def get_offset(self):
        level = len(self.path)-1
        if level > 5:
            level = 5
        return level

    def get_col(self):
        level = len(self.path)-1
        if level > 5:
            level = 5
        return 12 - level
