from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import CommentForm

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/post/list.html'


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) #4 posts on each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger: #if page not int return the 1st page
        posts = paginator.page(1)
    except EmptyPage: #if the number of the page is more than exist then return the very last page
        posts = paginator.page(pagination.num_pages)
    return render(request, 'blog/post/list.html', 
    {'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, slug=post, status='published', 
        publish__year=year, publish__month=month, 
        publish__day=day)       
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST': #user sent a comment
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid(): 
            new_comment = comment_form.save(commit=False) #comment is created but still not saved in db
            new_comment.post = post #tie up the comment to the current post
            new_comment.save() #saving the comment in db
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', locals())