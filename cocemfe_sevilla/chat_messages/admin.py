from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post_date', 'document')
    search_fields = ('id',)
    icon_name = 'comment'