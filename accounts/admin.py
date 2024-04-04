from django.contrib import admin as A
from django.contrib.auth.admin import UserAdmin as E
from.models import User,UserProfile as B
class C(A.StackedInline):model=B;can_delete=False;verbose_name_plural='profile'
class D(A.ModelAdmin):inlines=C,
A.site.register(User,D)