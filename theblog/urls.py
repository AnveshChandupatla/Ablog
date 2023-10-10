from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import TutorialHome,HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
# from django.template import 
urlpatterns = [
    
    path('',HomeView.as_view(), name="home"),
    path('Tutorialhome',TutorialHome.as_view(), name="tutorialhome"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit_post/<int:pk>', UpdatePostView.as_view(),name='edit_post'),
    path('article/remove/<int:pk>', DeletePostView.as_view(),name='delete_post'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)