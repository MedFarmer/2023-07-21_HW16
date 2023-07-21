from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profile, name='profile'),
    path('sign-in/', login, name='login'),
    path('save_text_file/', save_text_file, name='save_text_file')
]

