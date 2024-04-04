from django import forms as A
from django.contrib.auth import get_user_model as B
from django.contrib.auth.forms import UserChangeForm,UserCreationForm as C
from django.forms.models import inlineformset_factory
from.models import UserProfile as D
E=B()
class F(C):
	email=A.EmailField(required=True);password1=A.CharField(label='Password',widget=A.PasswordInput,required=True);password2=A.CharField(label='Confirm Password',widget=A.PasswordInput,required=True);username=A.CharField(required=True)
	class Meta:model=E;fields='first_name','last_name','username','email','password1','password2'
class G(A.ModelForm):
	class Meta:model=D;fields='picture','bio','phone','website','address'