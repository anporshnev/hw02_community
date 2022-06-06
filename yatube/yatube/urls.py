from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('posts.urls', namespace='index_posts')),
    path('group/<slug:slug>/', include('posts.urls', namespace='group_posts')),
    path('admin/', admin.site.urls),
]
