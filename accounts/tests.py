from django.contrib.auth import get_user_model as D
from django.test import TestCase as B
from django.urls import reverse as A
from.forms import ProfileForm as E
C=D()
class F(B):
	def test_login_redirect_if_user_not_logged_in(B):
		C=B.client.get(A('chat:home'));B.assertRedirects(C,'/accounts/login/?next=/')
		with B.settings(LOGIN_URL='/accounts/register/'):C=B.client.get('');B.assertRedirects(C,'/accounts/register/?next=/')
	def test_login_template(B):C=B.client.get(A('accounts:login'));B.assertTemplateUsed(C,'registration/login.html')
class G(B):
	def test_redirect_if_user_logged_in(B):D=C.objects.create(username='abc',email='abc@test.com');D.set_password('abc');D.save();B.client.login(username='abc',password='abc');E=B.client.get(A('accounts:register'));B.assertRedirects(E,A('chat:home'))
	def test_valid_registration(B):D={'username':'john','email':'john@test.com','first_name':'john','last_name':'doe','password1':'@secret123','password2':'@secret123'};E=B.client.post(A('accounts:register'),D);B.assertRedirects(E,A('chat:home'));B.assertEqual(C.objects.count(),1)
	def test_invalid_registration(B):
		C=[{'username':'john','email':'john@test.com','first_name':'john','last_name':'doe','password1':'secret12','password2':'secret123'},{'username':'john','email':'johntest.com','first_name':'john','last_name':'doe','password1':'secret123','password2':'secret123'},{'username':'!john','email':'john@test.com','first_name':'john','last_name':'doe','password1':'secret12','password2':'secret123'}]
		for D in C:E=B.client.post(A('accounts:register'),D);B.assertEqual(E.status_code,200)
	def test_register_page_templates(B):C=B.client.get(A('accounts:register'));B.assertTemplateUsed(C,'registration/register.html')
class H(B):
	def setUp(A):A.user=C.objects.create(username='john',email='john@test.com');A.user.set_password('secret');A.user.save();A.client.login(username='john',password='secret')
	def test_redirect_if_user_not_logged_in(B):B.client.logout();C=B.client.get(A('accounts:view-profile',args=('someUser',)));B.assertRedirects(C,f"{A('accounts:login')}?next={A('accounts:view-profile',args=('someUser',))}")
	def test_view_profile(B):E=C.objects.create(username='abc',email='abc@test.com');D=B.client.get(A('accounts:view-profile',args=('abc',)));B.assertEqual(D.status_code,200);B.assertTemplateUsed(D,'accounts/users_profile.html');B.assertTemplateUsed(D,'accounts/profile.html');B.assertEqual(D.context['user'],E);B.assertEqual(D.context['is_following'],False)
	def test_profile_edit_view(B):C=B.client.get(A('accounts:edit_profile'));B.assertEqual(C.status_code,200);B.assertTrue(isinstance(C.context['form'],E));B.assertTemplateUsed(C,'accounts/edit_profile.html')
	def test_profile_edit_success(B):D={'bio':'Testing the application','phone':'39239104831','website':'https://some.website.com','address':'Memory Loc 4'};E=B.client.post(A('accounts:edit_profile'),D);B.assertRedirects(E,A('accounts:view-profile',args=(B.user.username,)));B.user=C.objects.get(username=B.user.username);B.assertEqual(B.user.profile.phone,'39239104831');B.assertEqual(B.user.profile.bio,'Testing the application');B.assertEqual(B.user.profile.website,'https://some.website.com');B.assertEqual(B.user.profile.address,'Memory Loc 4')
class I(B):
	def setUp(A):A.user=C.objects.create(username='john',email='john@test.com');A.user.set_password('secret');A.user.save();A.client.login(username='john',password='secret');A.a_user=C.objects.create(username='a_',email='a@test.com');A.b_user=C.objects.create(username='b_',email='b@test.com');A.c_user=C.objects.create(username='c_',email='c@test.com');A.user.followers.add(A.a_user)
	def test_redirect_if_user_not_logged_in(B):B.client.logout();C=B.client.get(A('accounts:followers'));B.assertRedirects(C,f"{A('accounts:login')}?next={A('accounts:followers')}")
	def test_followers_view(B):C=B.client.get(A('accounts:followers'));B.assertTemplateUsed(C,'accounts/followers.html');B.assertEqual(len(C.context['users_followed']),1);B.assertEqual(len(C.context['unfollowed_users']),2)
	def test_add_followers_view(B):C=B.client.get(A('accounts:follow',args=('b_',)));B.assertRedirects(C,A('accounts:followers'));B.assertEqual(B.user.followers.count(),2)
	def test_remove_followers_view(B):C=B.client.get(A('accounts:unfollow',args=('a_',)));B.assertRedirects(C,A('accounts:followers'));B.assertEqual(B.user.followers.count(),0)