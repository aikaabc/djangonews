from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse #gives opportunity to get url after entering its name of draft and parameters
# from django.views.generic import DetailView

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'path/post_detail.html'
#     slug_field = 'title'


class Post(models.Model):
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
            self.publish.month, self.publish.day, self.slug])
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() #default manager
    published = PublishedManager() #my new manager

    class Meta:
        ordering = ('-publish',)

        def __str__(self):
            return self.title
