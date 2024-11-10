from django.urls import path

from blog import views as blog_views

app_name = "blog"
urlpatterns = [
    path("posts/", blog_views.post_list, name="post-list"),
]
