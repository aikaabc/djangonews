from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    url('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls', namespace='blog')),
]
