from django.db import models as A
from django.conf import settings as B
class C(A.Model):
	user=A.ForeignKey(B.AUTH_USER_MODEL,related_name='posts',on_delete=A.CASCADE);picture=A.ImageField(upload_to='posts',blank=True);text=A.TextField(max_length=2048,blank=True);posted_date=A.DateTimeField(auto_now_add=True)
	def __str__(A):return f"{A.user.username}'s post"
class D(A.Model):user=A.ForeignKey(B.AUTH_USER_MODEL,related_name='comments',on_delete=A.CASCADE);post=A.ForeignKey(C,related_name='comments',on_delete=A.CASCADE);text=A.TextField(max_length=2048,blank=True);comment_date=A.DateTimeField(auto_now_add=True)