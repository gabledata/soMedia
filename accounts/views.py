from datetime import datetime as B
import uuid as C
from django.contrib.auth import authenticate as O,get_user_model as P,login
from django.contrib.auth.decorators import login_required as F
from django.shortcuts import redirect as G,render as J
from django.urls import reverse as L
from django.http import HttpRequest as A
from soMedia.utils.event_tracking import get_device_id as D,send_analytics_payload,get_session_property as H,is_mobile as I
from.forms import ProfileForm as M,RegistrationForm as N
from.models import UserProfile as E
K=P()
def Q(request:A):
	A=request
	if A.user.is_authenticated:return G(L('chat:home'))
	if A.method=='POST':
		K=N(A.POST)
		if K.is_valid():M=K.save();M=O(username=A.POST['username'],password=A.POST['password1']);F,P=E.objects.get_or_create(user=A.user);send_analytics_payload({'tracks':[{'_type':'register','_dt':B.now(),'_source':'soMedia.web_backend','_uuid':C.uuid4(),'_version':'0.3.0','device_id':D(F),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','account_created':P,'username':F.user.username,'user_website':F.website,'user_bio':F.bio,'user_phone':F.phone,'user_address':F.address}]});login(A,M);return G(L('chat:home'))
	else:K=N()
	return J(A,'registration/register.html',{'form':K})
@F
def R(request:A,username):A=request;G=K.objects.get(username=username);L=A.user.is_following(G);F=E.objects.get(user=G);send_analytics_payload({'tracks':[{'_type':'view_profile','_dt':B.now(),'_source':'soMedia.web_backend','_uuid':C.uuid4(),'_version':'0.3.0','device_id':D(F),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':F.user.username,'user_website':F.website,'user_bio':F.bio,'user_phone':F.phone,'user_address':F.address}]});return J(A,'accounts/users_profile.html',{'user':G,'is_following':L})
@F
def S(request:A):
	A=request
	if A.method=='POST':
		K=M(A.POST,A.FILES,instance=A.user.profile)
		if K.is_valid():K.save();F=E.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'edit_profile','_dt':B.now(),'_source':'soMedia.web_backend','_uuid':C.uuid4(),'_version':'0.3.0','device_id':D(F),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':F.user.username,'user_website':F.website,'user_bio':F.bio,'user_phone':F.phone,'user_address':F.address}]});return G(L('accounts:view-profile',args=(A.user.username,)))
	else:K=M(instance=A.user.profile)
	return J(A,'accounts/edit_profile.html',{'form':K})
@F
def T(request:A):A=request;G=A.user.followers.all();H=K.objects.exclude(id__in=G).exclude(id=A.user.id);F=E.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'get_followers','_dt':B.now(),'_source':'soMedia.web_backend','_uuid':C.uuid4(),'_version':'0.3.0','device_id':D(F),'ip_address':A.get_host(),'path':A.get_full_path(),'language':'en-us','username':F.user.username,'user_website':F.website,'user_bio':F.bio,'user_phone':F.phone,'user_address':F.address}]});return J(A,'accounts/followers.html',{'users_followed':G,'unfollowed_users':H})
@F
def U(request:A,username):A=request;A.user.followers.add(K.objects.get(username=username));F=E.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'follow_user','_dt':B.now(),'_source':'soMedia.web_backend','_uuid':C.uuid4(),'_version':'0.3.0','device_id':D(F),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':F.user.username,'user_website':F.website,'user_bio':F.bio,'user_phone':F.phone,'user_address':F.address}]});return G('accounts:followers')
def V(request:A,username):A=request;A.user.followers.remove(K.objects.get(username=username));F=E.objects.get(user=A.user);send_analytics_payload({'tracks':[{'_type':'unfollow_user','_dt':B.now(),'_source':'soMedia.web_backend','_uuid':C.uuid4(),'_version':'0.3.0','device_id':D(F),'session_id':H(A,'session_id'),'ip_address':A.get_host(),'path':A.get_full_path(),'is_secure':A.is_secure(),'is_mobile':I(A),'language':'en-us','username':F.user.username,'user_website':F.website,'user_bio':F.bio,'user_phone':F.phone,'user_address':F.address}]});return G('accounts:followers')