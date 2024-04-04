from django.contrib.auth import get_user_model as A
B=A()
class C:
	def _create_user_and_login(C,username):A=B.objects.create(username=username,email='john@test.com');A.set_password('secret');A.save();C.client.login(username='john',password='secret');return A
	def _create_user(C,username,password):A=B.objects.create(username=username,email='john@test.com');A.set_password(password);A.save();return A