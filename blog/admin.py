from django.contrib import admin
from .models import Post, Comment

'''this makes the model visible in the admin page, and provides all the
administrative accesses like edit, delete, add and so on'''
admin.site.register(Post)

admin.site.register(Comment)
