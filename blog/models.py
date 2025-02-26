import os
import uuid

from django.db import models
from django.utils import timezone


def post_image_path(instance, filename):
    new_filename = f"{uuid.uuid4()}{os.path.splitext(filename)[1]}"
    now = timezone.now()
    return f"post_image/{now.strftime('%Y/%m/%d')}/{new_filename}"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    class Status(models.TextChoices):
        PUBLIC = "public", "Public"
        PRIVATE = "private", "Private"

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(
        max_length=7,
        choices=Status,
        default=Status.PUBLIC,
    )
    # image = models.ImageField(blank=True, null=True, upload_to="posts/image/%Y/%m/%d/")
    image = models.ImageField(blank=True, null=True, upload_to=post_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",
    )

    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    nick_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self) -> str:
        return self.content
