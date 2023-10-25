from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, PostBlog, UpdateBlog, DeleteBlog

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', ArticleDetailView.as_view(), name ="blog-details"),
    path('post_blog/', PostBlog.as_view(), name='post'),
    path('blog/edit/<int:pk>', UpdateBlog.as_view(), name='update_blog'),
    path('blog/<int:pk>/delete', DeleteBlog.as_view(), name='delete_blog')
]
