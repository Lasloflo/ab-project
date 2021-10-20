from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('gallery/', gallery, name='gallery'),
    path('video/', video, name='video'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('messagesent/', sentmessage, name='sentmessage'),
]