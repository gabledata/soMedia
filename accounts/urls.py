from django.urls import path as A,include as C
from.import views as B
D='accounts'
E=[A('',C('django.contrib.auth.urls')),A('register/',B.register,name='register'),A('followers/',B.followers,name='followers'),A('my-profile/edit/',B.edit_profile,name='edit_profile'),A('profile/<username>/',B.profile,name='view-profile'),A('users/follow/<username>/',B.follow,name='follow'),A('users/unfollow/<username>/',B.unfollow,name='unfollow')]