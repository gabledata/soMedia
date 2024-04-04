F=isinstance
from django.test import Client,TestCase as B
from django.urls import reverse as A
from libs.tests import TestMixin as C
from.forms import CommentForm as G,PostForm as H
from.models import Comment as D,Post as E
class I(B,C):
	def test_home_page_rendered(B):D=B._create_user_and_login('john');C=B.client.get(A('chat:home'));B.assertTemplateUsed(C,'chat/home.html');B.assertTrue(F(C.context['comment_form'],G));B.assertEqual(len(C.context['posts']),0)
	def test_redirect_if_user_is_not_logged_in(B):C=B.client.get(A('chat:home'));B.assertRedirects(C,f"{A('accounts:login')}?next={A('chat:home')}")
class J(B,C):
	def test_post_redirect_not_logged_in(B):C=B.client.get(A('chat:add_post'));B.assertRedirects(C,f"{A('accounts:login')}?next={A('chat:add_post')}")
	def test_view_get(B):D=B._create_user_and_login('john');C=B.client.get(A('chat:add_post'));B.assertTrue(F(C.context['form'],H));B.assertTemplateUsed('chat/add_post.html')
	def test_valid_add_post(B):D=B._create_user_and_login('john');C=B.client.post(A('chat:add_post'),data={'post':'new post'});B.assertRedirects(C,A('chat:home'));B.assertEqual(E.objects.count(),1)
class K(B,C):
	def setUp(A):A.user=A._create_user_and_login('john');A._post=E.objects.create(user=A.user,text='some new post')
	def test_only_post_allowed(B):C=B.client.get(A('chat:add_comment',args=(B._post.id,)));B.assertEqual(C.status_code,405)
	def test_comment(B):C=B.client.post(A('chat:add_comment',args=(B._post.id,)),data={'text':'new comment'});B.assertRedirects(C,A('chat:home'));B.assertEqual(D.objects.count(),1);E=D.objects.last();B.assertEqual(B._post,E.post)