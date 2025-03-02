from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from blog.filters import PostFilter
from blog.forms import CommentForm, PostForm
from blog.models import Category, Post
from core.forms import DeleteConfirmForm


# Create your views here.
def post_list(request):
    # Remove the following because we add the filter.
    # posts = Post.objects.select_related("category").prefetch_related("tags")
    # return render(request, "blog/post_list.html", {"posts": posts})

    post_filter = PostFilter(
        request.GET or None,
        queryset=Post.objects.select_related("category").prefetch_related("tags"),
    )
    return render(request, "blog/post_list.html", {"post_filter": post_filter})


@login_required
def post_create(request):
    # form = PostForm(request.POST or None)
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        # print("view", form.cleaned_data)
        form.save()
        # post = form.save(commit=False)
        # post.category = Category.objects.first()
        # post.save()
        # # U should add the following line, if there is a field with many-to-many.
        # form.save_m2m()

        messages.success(request, "Post create success.")
        return redirect("blog:post-list")

    return render(request, "blog/post_create.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()

    return render(
        request, "blog/post_detail.html", {"post": post, "comment_form": comment_form}
    )


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, "Post update success.")
        return redirect("blog:post-detail", pk=pk)

    return render(request, "blog/post_update.html", {"form": form})


@login_required
def post_delete(request, pk):
    form = DeleteConfirmForm(request.POST or None)
    post = get_object_or_404(Post, pk=pk)

    if form.is_valid():
        post.delete()
        messages.success(request, "刪除成功")
        return redirect("blog:post-list")
    return render(request, "blog/post_delete.html", {"form": form, "post": post})


@login_required
def post_create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        messages.success(request, "留言成功")

    return redirect("blog:post-detail", pk=post_pk)
