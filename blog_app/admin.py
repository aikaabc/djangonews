from django.contrib import admin
from .models import Post

# admin.site.register(Post)
@admin.register(Post) #this decorator does the same work as line 4
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',) #allows to display fields of the model,that we want to see
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
