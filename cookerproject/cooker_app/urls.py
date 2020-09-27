from django.urls import path
from .import views
app_name = 'cooker_app'
from .decorators import check_recaptcha
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.single, name='single'),
    path('category/', views.category, name='category'),
    path('category/<str:slugname>/', views.catarticles, name='catarticles'),
    path('search/', views.post_search, name='post_search'),
    path('comment/<int:article_id>/', views.add_comment, name='add_comment'),
    path('register/', check_recaptcha(views.SiteAppRegisterFormView.as_view()), name="register"),
    path('logout/', views.Logout, name='logout'),
]

