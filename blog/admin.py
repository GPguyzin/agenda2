from django.contrib import admin
from .models import Post, Comment, PostCd


admin.site.register(Post)
admin.site.register(PostCd)
admin.site.register(Comment)