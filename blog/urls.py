from django.urls import path

from blog import views as blog_views

app_name = "blog"
urlpatterns = [
    path("posts/", blog_views.post_list, name="post-list"),
    path("posts/create/", blog_views.post_create, name="post-create"),
    path("posts/<int:pk>/", blog_views.post_detail, name="post-detail"),
    path("posts/<int:pk>/update/", blog_views.post_update, name="post-update"),
]
