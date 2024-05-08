from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('login',views.handlelogin,name='login'),
    path('signup', views.signup, name='signup'),
]
