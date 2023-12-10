from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name='login'),

]
