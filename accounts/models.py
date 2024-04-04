from django.db import models as A
from django.contrib.auth.models import AbstractUser as C
from django.db.models.signals import post_save as D
from django.dispatch import receiver as E
class B(C):
	followers=A.ManyToManyField('self',blank=True)
	def is_following(A,user):return user in A.followers.all()
class F(A.Model):
	user=A.OneToOneField(B,on_delete=A.CASCADE,related_name='profile',verbose_name='other Details');picture=A.ImageField(upload_to='profile_pictures',blank=True,null=True);website=A.URLField(blank=True);bio=A.TextField(blank=True);phone=A.CharField(max_length=11,blank=True);address=A.CharField(max_length=100,blank=True)
	def __str__(A):return A.user.username
@E(D,sender=B)
def G(sender,**A):
	if A['created']:B=F.objects.get_or_create(user=A['instance'])