from django import forms as A
from.models import Comment as B,Post
class C(A.ModelForm):
	class Meta:model=Post;fields='picture','text'
class D(A.Form):
	text=A.CharField(label='Comment',widget=A.Textarea(attrs={'rows':3}))
	def save(A,post,user):C=B.objects.create(text=A.cleaned_data.get('text',None),post=post,user=user)