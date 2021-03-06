from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_summernote.admin import SummernoteModelAdmin

from .models import Comment, Post, Tag, User

admin.site.register(User, UserAdmin)


@admin.register(Post, Comment, Tag)
class BulkAdmin(SummernoteModelAdmin):
    pass
