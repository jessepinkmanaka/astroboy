from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    caption = models.TextField()
    banner = models.ImageField(upload_to='banners/')  # Required banner image
    body_markdown = models.TextField(blank=True)  # Markdown content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')
    identifier = models.CharField(max_length=50, blank=True, help_text="Unique identifier for embedding in markdown, e.g. image1")
    caption = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.identifier:
            # Find the next available identifier for this post
            existing = self.post.images.values_list('identifier', flat=True)
            i = 1
            while True:
                candidate = f"image{i}"
                if candidate not in existing:
                    self.identifier = candidate
                    break
                i += 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.post.title} ({self.identifier})"
