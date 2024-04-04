from datetime import datetime as D
import uuid as E
from django.contrib.auth.decorators import login_required as A
from django.shortcuts import redirect as J,render as K
from django.urls import reverse as N
from django.views.decorators.http import require_POST as B
from accounts.models import UserProfile as F
from soMedia.utils.event_tracking import get_device_id as G,send_analytics_payload,get_session_property as H,is_mobile as I
from.forms import CommentForm as C,PostForm as L
from.models import Post as M
@A
def O(request):A=request;J=list(A.user.followers.all());J.append(A.user);L=M.objects.filter(user__in=J).order_by('-posted_date');N=C();B=F.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'homepage_viewed','_dt':D.now(),'_source':'soMedia.web_backend','_uuid':E.uuid4(),'_version':'0.3.0','device_id':G(B),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':B.user.username,'user_website':B.website,'user_bio':B.bio,'user_phone':B.phone,'user_address':B.address}]});return K(A,'chat/home.html',{'posts':L,'comment_form':N})
@A
def P(request):
	A=request
	if A.method=='POST':
		C=L(A.POST,A.FILES)
		if C.is_valid():M=C.save(commit=False);M.user=A.user;M.save();B=F.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'add_post','_dt':D.now(),'_source':'soMedia.web_backend','_uuid':E.uuid4(),'_version':'0.3.0','device_id':G(B),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':B.user.username,'user_website':B.website,'user_bio':B.bio,'user_phone':B.phone,'user_address':B.address}]});return J('chat:home')
	else:C=L()
	return K(A,'chat/add_post.html',{'form':C})
@A
@B
def Q(request,post_id):
	A=request;K=C(A.POST)
	if K.is_valid():L=K.save(M.objects.get(id=post_id),A.user);B=F.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'add_comment','_dt':D.now(),'_source':'soMedia.web_backend','_uuid':E.uuid4(),'_version':'0.3.0','device_id':G(B),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':B.user.username,'user_website':B.website,'user_bio':B.bio,'user_phone':B.phone,'user_address':B.address}]})
	return J(N('chat:home'))