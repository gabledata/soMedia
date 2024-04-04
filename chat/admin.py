from django.contrib import admin as A
from.models import Comment as B,Post
A.site.register(B)
A.site.register(Post)