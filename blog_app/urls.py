from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),#we use <> so the <parameter> will be defined as readable url with integers 
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    ] 