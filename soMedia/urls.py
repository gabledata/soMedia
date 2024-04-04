from django.contrib import admin
from django.urls import path as A,include as B
from django.conf import settings as C
from django.conf.urls.static import static as D
E=[A('admin/',admin.site.urls),A('accounts/',B('accounts.urls')),A('',B('chat.urls'))]+D(C.MEDIA_URL,document_root=C.MEDIA_ROOT)