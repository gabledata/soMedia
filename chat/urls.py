from django.urls import path as A
from.import views as B
C='chat'
D=[A('',B.home,name='home'),A('posts/add',B.add_post,name='add_post'),A('comments/add/<post_id>',B.add_comment,name='add_comment')]