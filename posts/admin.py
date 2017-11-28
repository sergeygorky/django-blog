from django.contrib import admin

# Register your models here.
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_brief', 'updated', 'timestamp']
    list_display_links = ['updated', 'timestamp']
    list_editable = ['title']
    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'content']

    def content_brief(self, post):
        return post.content.split('.')[0] + '.'


admin.site.register(Post, PostModelAdmin)
