from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from post.models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'created', 'updated', 'customer_link',)
    list_filter = ('created',)

    def customer_link(self, obj):
        cust = obj.author
        url = reverse("admin:authentication_user_changelist") + str(cust.id)
        return format_html(f'<a href="{url}">{cust.username}</a>')

    customer_link.short_description = 'Автор'


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', )
