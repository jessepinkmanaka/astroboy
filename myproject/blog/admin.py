from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'created_at')
    search_fields = ('title', 'caption', 'content')
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(PostImage)