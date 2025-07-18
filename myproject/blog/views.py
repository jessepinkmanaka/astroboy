from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
from django.utils.safestring import mark_safe

# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    body = post.body_markdown or ''
    # Replace image identifiers with actual image URLs (for markdown image syntax)
    for img in post.images.all():
        body = body.replace(f'{{{{{img.identifier}}}}}', img.image.url)
    post_html = mark_safe(markdown.markdown(body, extensions=["extra"]))
    return render(request, 'blog/post_detail.html', {'post': post, 'post_html': post_html})
