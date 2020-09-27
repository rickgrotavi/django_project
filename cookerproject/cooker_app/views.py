from django.views import View
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.views.generic.edit import FormView
 
from cooker_app.models import Article
from cooker_app.models import Category
from cooker_app.models import Comment

from .forms import SearchForm, CommentForm, RegForm
 

class SiteAppRegisterFormView(FormView):
    form_class = RegForm
    success_url = "registration/login.html"
    template_name = "registration/register.html"

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form.save()
            return super(SiteAppRegisterFormView, self).form_valid(form)
        else:
            return render(self.request, 'registration/register.html', self.get_context_data())                    
        
def Logout(request):
    auth.logout(request)
    return render(request, "registration/logout.html")

def home(request):
    postList = Article.objects.filter(visible='1')
    paginator = Paginator(postList, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
 
    context = {
        "posts": posts,
        "title": "Главная страница",
        "desc": "Описание",
        "key": "ключевые, слова, страницы",
    }
    return render(request, "partial/home.html", context)
 

def single(request, id=None):
    post = get_object_or_404(Article, id=id)
    comments = post.comment_set.all().order_by('path')
    nextc = post.get_absolute_url()
    user = auth.get_user(request)
    idpost =  id
    context = {
        "post": post,
        "comments": comments,
        "next": nextc,
    }
    if user.is_authenticated:
        form = CommentForm
        context.update({'form':form})
    return render(request, "partial/single.html", context)

def category(request):
    catList = Category.objects.all()
    paginator = Paginator(catList, 4)
    page = request.GET.get('page')
    lists = paginator.get_page(page)

    context = {
        "lists": lists,
    }
    return render(request, "partial/category.html", context)

def catarticles(request, slugname):
    category = Category.objects.get(slug = slugname)
    postList = Article.objects.filter(category=category)
    paginator = Paginator(postList, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
 
    context = {
        "posts": posts,
        "title": "Главная страница",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request,"partial/catarticles.html", context)

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            title_vector = SearchVector('title', weight='A')
            cocntent_vetor = SearchVector('content', weight='B')
            vectors = title_vector + cocntent_vetor
            results = Article.objects.annotate(
                search=SearchVector(vectors)).filter(search = query)
            
    return render(request, "partial/search.html", {
        'form': form,
        'query': query,
        'results': results,
    })


    
@login_required
@require_http_methods(["POST"])
def add_comment(request, article_id):
    form = CommentForm(request.POST)
    article = get_object_or_404(Article, id=article_id)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.article_id = article
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()

        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)
        
        comment.save()
    return redirect(article.get_absolute_url())
